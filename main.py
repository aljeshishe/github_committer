import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def get_pixels(text: str) -> list[tuple[int, int, int]]:
    width, height = 700, 7
    canvas = Image.new('RGB', (width, height), 'black')

    draw = ImageDraw.Draw(canvas)
    draw.text((0, -3), text, fill="white")
    canvas.save('print_test.png')

    pixels = [canvas.getpixel((x, y))
              for x in range(width)
              for y in range(height)]
    return pixels

def get_commit_count(start_date, pixels, max_commits):
    offset_days = (datetime.datetime.utcnow() - start_date).days
    pixel = pixels[offset_days]
    MAX_PIXEL = (255,255,255)
    commits = 1.0 * max_commits * sum(pixel) / sum(MAX_PIXEL)
    return int(commits)


if __name__ == '__main__':
    START_DATE = '2023-06-10'
    pixels = get_pixels(text='python')
    start_date = datetime.datetime.strptime(START_DATE, '%Y-%m-%d')
    count = get_commit_count(start_date=start_date, pixels=pixels, max_commits=45)
    print(count)