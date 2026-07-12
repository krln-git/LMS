with open("lms/templates/video.html", "r") as f:
    content = f.read()

content = content.replace(
    '<button class="thumbs-up-btn">',
    '<button class="thumbs-up-btn" aria-label="${_(\'Thumbs up\')}">'
)
content = content.replace(
    '<span class="icon fa fa-thumbs-o-up thumbs-up-icon"></span>',
    '<span class="icon fa fa-thumbs-o-up thumbs-up-icon" aria-hidden="true"></span>'
)
content = content.replace(
    '<button class="thumbs-down-btn">',
    '<button class="thumbs-down-btn" aria-label="${_(\'Thumbs down\')}">'
)
content = content.replace(
    '<span class="icon fa fa-thumbs-o-down thumbs-down-icon"></span>',
    '<span class="icon fa fa-thumbs-o-down thumbs-down-icon" aria-hidden="true"></span>'
)

with open("lms/templates/video.html", "w") as f:
    f.write(content)
