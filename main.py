from src.analyzer import Analyzer
def main():
    try:
        with open("tests/log1.txt", "r") as file:
            analyzer = Analyzer(file)
            analyzer.analyze()
    except FileNotFoundError:
        print("File Not Found")
        return  

    return

if __name__ == "__main__":
    main()