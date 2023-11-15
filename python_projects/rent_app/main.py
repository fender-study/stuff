from scraper import Scrape
from filler import FormFiller

def main():
    data = Scrape()

    my_l = data.combined_list()
    filler = FormFiller()
    for item in my_l:
        filler.fill_form(item)

    filler.close_window()


if __name__ == "__main__":
    main()
