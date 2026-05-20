"""
Image Comparison Tool for HW4 : CSE 163 NCHS
"""


from PIL import Image, ImageChops


def compare_images(actual, expected, diff_file):
    """
    Description: compares two images and highlights
    absolute value of the pixel-by-pixel difference between the two images.
    Save masked diff_file
    Parameters:
        - (String) actual : filename of student image file
        - (String) expected : filename of the expected image
        - (String) diff_file : filename to store the differences
    """

    # Loading images with format of RGB
    expected = Image.open(expected).convert('RGB')
    student = Image.open(actual).convert('RGB')

    # ABS Difference
    diff = ImageChops.difference(expected, student)
    diff_RGBA = diff.convert("RGBA")

    # Changing masked color to RED & making black background transparent
    datas = diff_RGBA.getdata()
    replaced_data = []

    for itexem in datas:
        if itexem[0] == 0 and itexem[1] == 0 and itexem[2] == 0:
            replaced_data.append((255, 255, 255, 0))
        else:
            replaced_data.append((255, 0, 0, 255))
    diff_RGBA.putdata(replaced_data)

    # Overlaying ABS difference with source image
    final_masked = expected.convert("RGBA")
    final_masked.alpha_composite(diff_RGBA)

    # Save final_maksed image at compare/
    final_masked.save(diff_file)


def get_diff_name(filename):
    # generate difference filename
    last_dot = filename.rfind('.')
    diff_file = filename[: last_dot] + '_diff.' + filename[last_dot + 1:]
    return diff_file


def compare_image(filename):
    '''
    Generates the 3 filenames for actual, expected and diff_file 
    using relative paths from filename.
    filename may be a full path or relative path
        - actual is the filename, untouched
        - expected is in the current working directory/expected/filename
        - diff is in the current working directory/compare/filename
    '''
    last_slash = filename.rfind('/')
    # keep the part leading up to the last slash. Assume no slash
    leading = ''
    last = filename
    if last_slash != -1:
        last = filename[last_slash + 1:]
        leading = filename[:last_slash] + '/'
    expected = leading + 'expected/' + last
    compare = leading + 'compare/' + last
    compare_images(filename, expected, compare)


def compare_hw4_images():
    compare_image("bar_chart_high_school.png")
    compare_image("line_plot_bachelors.png")
    compare_image("plot_hispanic_min_degree.png")


if __name__ == '__main__':
    compare_hw4_images()