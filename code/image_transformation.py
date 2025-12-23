from PIL import Image, ImageFilter
import os

def apply_gaussian_blur(
    input_path: str,
    output_path: str = None,
    radius: float = 1.5
):
    """
    Apply Gaussian blur to an image.

    Parameters
    ----------
    input_path : str
        Path to the input PNG file.
    output_path : str, optional
        Path to save the output image.
    radius : float
        Blur radius (standard deviation in pixels).
        Typical values:
            0.5–1.0  : light blur
            1.5–3.0  : moderate blur
            4.0+     : heavy blur

    Returns
    -------
    str
        Path to the saved image.
    """
    if radius < 0:
        raise ValueError("radius must be non-negative")

    img = Image.open(input_path)
    blurred = img.filter(ImageFilter.GaussianBlur(radius=radius))

    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_blur{ext}"

    blurred.save(output_path)
    return output_path




def lower_resolution(
    input_path: str,
    output_path: str = None,
    scale: float = 0.5,
    resample=Image.BICUBIC
):
    """
    Downscale a PNG image to lower its resolution.

    Parameters
    ----------
    input_path : str
        Path to the input PNG file.
    output_path : str, optional
        Path to save the output image. If None, auto-generates one.
    scale : float
        Scaling factor (e.g., 0.5 halves both width and height).
    resample :
        PIL resampling filter (NEAREST, BILINEAR, BICUBIC, LANCZOS).

    Returns
    -------
    str
        Path to the saved image.
    """
    if not (0 < scale < 1):
        raise ValueError("scale must be between 0 and 1")

    img = Image.open(input_path)
    w, h = img.size
    new_size = (int(w * scale), int(h * scale))

    img_low = img.resize(new_size, resample=resample)

    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_lowres{ext}"

    img_low.save(output_path)
    return output_path




def non_uniform_scale(
    input_path: str,
    output_path: str = None,
    scale_x: float = 1.0,
    scale_y: float = 1.0,
    resample=Image.BICUBIC
):
    """
    Apply non-uniform scaling to an image (independent x/y scaling).

    Parameters
    ----------
    input_path : str
        Path to the input PNG file.
    output_path : str, optional
        Path to save the output image.
    scale_x : float
        Horizontal scaling factor (>1 stretches, <1 compresses).
    scale_y : float
        Vertical scaling factor (>1 stretches, <1 compresses).
    resample :
        PIL resampling filter.

    Returns
    -------
    str
        Path to the saved image.
    """
    if scale_x <= 0 or scale_y <= 0:
        raise ValueError("scale_x and scale_y must be positive")

    img = Image.open(input_path)
    w, h = img.size

    new_w = int(w * scale_x)
    new_h = int(h * scale_y)

    img_scaled = img.resize((new_w, new_h), resample=resample)

    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_nonuniform{ext}"

    img_scaled.save(output_path)
    return output_path


def add_watermark(
    input_path: str,
    watermark_path: str,
    output_path: str = None,
    position: str = "bottom_right",
    scale: float = 0.2,
    opacity: float = 0.5,
    margin: int = 10
):
    """
    Add a watermark image onto a PNG image.

    Parameters
    ----------
    input_path : str
        Path to the input PNG.
    watermark_path : str
        Path to the watermark PNG (should support transparency).
    output_path : str, optional
        Path to save the output image.
    position : str
        One of: 'top_left', 'top_right', 'bottom_left', 'bottom_right', 'center'
    scale : float
        Relative size of watermark w.r.t. image width (e.g., 0.2 = 20% width).
    opacity : float
        Watermark opacity in [0, 1].
    margin : int
        Margin (pixels) from edges.

    Returns
    -------
    str
        Path to the saved image.
    """
    if not (0 <= opacity <= 1):
        raise ValueError("opacity must be between 0 and 1")

    base = Image.open(input_path).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")

    bw, bh = base.size
    ww = int(bw * scale)
    wh = int(ww * watermark.height / watermark.width)

    watermark = watermark.resize((ww, wh), Image.BICUBIC)

    # Adjust opacity
    if opacity < 1:
        alpha = watermark.split()[3]
        alpha = alpha.point(lambda p: int(p * opacity))
        watermark.putalpha(alpha)

    positions = {
        "top_left": (margin, margin),
        "top_right": (bw - ww - margin, margin),
        "bottom_left": (margin, bh - wh - margin),
        "bottom_right": (bw - ww - margin, bh - wh - margin),
        "center": ((bw - ww) // 2, (bh - wh) // 2),
    }

    if position not in positions:
        raise ValueError(f"Invalid position: {position}")

    base.paste(watermark, positions[position], watermark)

    if output_path is None:
        base_name, ext = os.path.splitext(input_path)
        output_path = f"{base_name}_watermarked{ext}"

    base.convert("RGB").save(output_path)
    return output_path