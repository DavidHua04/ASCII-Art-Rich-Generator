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
