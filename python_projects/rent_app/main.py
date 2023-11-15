from scraper import Scrape
from filler import FormFiller
# TODO 1: Create a list of links for all the listings you scraped. e.g.
# TODO 2: Create a list of prices for all the listings you scraped. e.g.
# TODO 3: Create a list of addresses for all the listings you scraped. e.g.
# TODO 4: Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its
#  price/address/link added to the form. You will need to fill in a new form for each new listing. e.g.
# TODO 5: Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the
#  responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.


def main():
    data = Scrape()

    my_l = data.combined_list()
    filler = FormFiller()
    for item in my_l:
        filler.fill_form(item)

    filler.close_window()


if __name__ == "__main__":
    main()
