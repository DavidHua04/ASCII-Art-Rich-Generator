# ASCII-Art-Rich-Generator

1. **Text To Image Converter**: Take in texts and convert it into Image. There should be one parameter for each dimensions to control the output image:
      1. Rendering Properties (How ASCII is rendered when converting to image)
          - Font family
          - Character spacing
          - Line spacing
          - Canvas width and height (e.g., 40 / 80 / 120 chars*10 / 20 / 30 lines)
          - background color


2. **ASCII Art Rich Generator**: Take in an Image and convert it into ASCII art of selected type. There should be one parameter for each dimensions to control the output ASCII Art text. All dimensions are:
      1. Character Semantics (What characters are made of)
          - Meaningless symbols (#$%&)
          - Random neutral words
          - Positive words
          - Negative / toxic words
          - Rare vs common words

      2. Language Properties (if we are not choosing Meaningless Symbols in Character Semantics part)
          - English / Chinese (fullwidth characters) / Hebrew (Abjad, write and read  from right to left)
          - Multilingual mixtures

3. **Image Transformer**: Take in an image and transform it by applying one of the follow:
          - Resolution: high / medium / low
          - Non-uniform scaling (stretch/compress)
          - Gaussian blur
          - Grayscale vs RGB
          - Contrast changes
          - Waterprint