def main():
    pass


if __name__ == "__main__":
    main()


class Theory:
    def __init__(self, content):
        self.content = content


class Test:
    def __init__(self, test: dict[str, str]):
        self.test = test


class Lesson:
    def __init__(self, theory, tests: list[Test]):
        self.theory = theory
        self.tests = tests


class Level:
    def __init__(self, lessons: list[Lesson]):
        self.lessons = lessons


class Topic:
    def __init__(self, levels: list[Level]):
        self.levels = levels


class Chapter:
    def __init__(self, topics: list[Topic]):
        self.topics = topics
