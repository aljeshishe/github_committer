from PIL import Image, ImageDraw

# Create a blank canvas with a white background
canvas = Image.new('RGB', (70, 7), (255, 255, 255))

# Create a draw object
draw = ImageDraw.Draw(canvas)

# Define the text and font
text = "hello"
font_size = 20  # Adjust font size as needed

# Calculate the position to center the text
text_width, text_height = draw.textsize(text)
x = (canvas.width - text_width) // 2
y = (canvas.height - text_height) // 2

# Draw the text on the canvas
draw.text((x, y), text, fill=(0, 0, 0))  # Using black color for text

# Save the canvas as an image file
canvas.save('canvas.png')

# Get the colors of each pixel in the canvas
pixels = list(canvas.getdata())

# Display the colors
for pixel in pixels:
    print(pixel)

