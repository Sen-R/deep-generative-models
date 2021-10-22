import math
import matplotlib.pyplot as plt


def show_examples(data, examples=50, ncols=10, **kwargs):
    if not hasattr(data, "shape"):
        # See if it is a tuple, dict or dataset and convert if possible.
        if hasattr(data, "keys"):
            show_examples(data["image"], examples, ncols, **kwargs)
        elif isinstance(data, tuple):
            show_examples(data[0], examples, ncols, **kwargs)
        else:  # Assume it's a dataset
            show_examples(next(iter(data)), examples, ncols, **kwargs)
    else:
        if hasattr(data, "numpy"):
            # Convert tensors to numpy
            data = data.numpy()
        examples = min(examples, len(data))
        nrows = math.ceil(examples / ncols)
        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, **kwargs)
        for image, ax in zip(data, axs.flatten()):
            ax.imshow(image.squeeze(), cmap="gist_gray")
            ax.axis("off")
        fig.subplots_adjust(wspace=0, hspace=0)
        plt.show()
