from jinja2 import Template
import pathlib
from pathlib import Path
import sys
import os


HTML_OUTPUT_FILE_NAME = "index.html"

photo_album_html = """
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ album_name }}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>

<body>
  <div class="container-fluid pb-3">
    <h1>{{ album_name }}</h1>
  </div>

  <div class="container-fluid text-center">
    <!-- Gallery -->
    <div class="row">      

      {% for imageFile in image_list %}
      <div class="col-lg-4 col-md-6 col-xs-12 mb-4 mb-lg-0">
        <img loading="lazy" src="{{ imageFile }}" class="w-100 shadow-1-strong rounded mb-4" />
      </div>
      {% endfor %}

    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
    crossorigin="anonymous"></script>
</body>

</html>
"""


def get_all_files_from_dir(dir: str) -> list[Path]:
    file_list = []
    for f in sorted(pathlib.Path(dir).iterdir(), key=os.path.getmtime):
        if f.is_file():
            file_list.append(f.name)

    return file_list


def write_to_html(html_output: str, output_file_name: str):
    # to save the results
    with open(output_file_name, "w") as fh:
        fh.write(html_output)


def build_html(album_name: str, image_list: list[str]) -> str:
    t = Template(photo_album_html)
    html_output = t.render(album_name=album_name, image_list=image_list)
    return html_output


if __name__ == "__main__":
    num_params = len(sys.argv)
    prog = sys.argv[0]
    if num_params < 3:
        print("Usage:", prog, '[album_name] [image_directory]')
        sys.exit()

    album_name = sys.argv[1]
    image_dir = sys.argv[2]

    files = get_all_files_from_dir(image_dir)
    html_output = build_html(album_name, files)

    output_html_file = os.path.join(image_dir, HTML_OUTPUT_FILE_NAME)
    write_to_html(html_output, output_html_file)



