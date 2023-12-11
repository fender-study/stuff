from follower import InstaFollower


def main():
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()


if __name__ == "__main__":
    main()