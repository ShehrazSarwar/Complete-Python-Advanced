# Compile-time Polymorphism
# Python doesn't support true method overloading like Java or C++.
# However, we can achieve similar behavior using:
# Default Arguments & Variable-Length Arguments (*args)

# Default Arguments
class VideoEditor:
    @staticmethod       #-------> Make method static if there is no need of self
    def export(resolution="1080p"):
        print(f"Exporting video in {resolution} resolution.")

editor = VideoEditor()
editor.export()
editor.export("4K")

print("-"*20)


# Variable-Length Arguments (*args)
class VideoEditor:
    @staticmethod       #-------> Make method static if there is no need of self
    def export(*args):  # *args can take as many as arguments
        if len(args) == 1:
            print(f"Exporting video in {args[0]} resolution.")
        elif len(args) == 2:
            print(f"Exporting {args[1]} video in {args[0]} resolution.")
        else:
            print("Invalid number of arguments.")


editor = VideoEditor()
editor.export()
editor.export("4K")
editor.export("Cinematic","1080p")