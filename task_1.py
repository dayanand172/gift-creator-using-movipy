from moviepy.editor import ImageSequenceClip
import os


def create_gif_from_images(image_folder, gif_name, fps=10):
    image_files = sorted(
        [
            os.path.join(image_folder, file)
            for file in os.listdir(image_folder)
            if file.endswith(("jpeg", "png", "jpg"))
        ]
    )

    clip = ImageSequenceClip(image_files, fps=fps)

    output_gif = f"{gif_name}.gif"
    clip.write_gif(output_gif, fps=fps)
    print(f"GIF '{output_gif}' created successfully!")


images_folder = "C:\\Users\\deepa\\Desktop\\grow_more\\img"
gif_name = "output_gif"

create_gif_from_images(images_folder, gif_name)
