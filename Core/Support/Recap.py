# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Support import Font
from Core.Support import Language
from Core.Support import Encoding
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Stats:

    @staticmethod
    def Hypotesys(Params, username, report):
        sleep(2)
        private = Params[0]
        if private == "False":
            Followers = Params[1]
            Posts = Params[2]
            FollowN = float(Followers.replace(",", ''))
            FollowConv = int(FollowN)
            PostsN = float(Posts.replace(",", ''))
            PostsConv = int(PostsN)
            if FollowConv >= 0 and FollowConv <= 700:
                if PostsConv >= 0 and PostsConv <= 30:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "LowLow").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "LowLow").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
                elif PostsConv > 30 and PostsConv <= 100:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "LowMid").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "LowMid").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
                elif PostsConv > 100:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "LowHigh").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "LowHigh").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
            elif FollowConv > 700 and FollowConv <= 150000:
                if PostsConv >= 0 and PostsConv <= 30:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "MidLow").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "MidLow").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
                elif PostsConv > 30 and PostsConv <= 100:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "MidMid").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "MidMid").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
                elif PostsConv > 100:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "MidHigh").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "MidHigh").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))

            elif FollowConv > 150000:
                if PostsConv >= 0 and PostsConv <= 30:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "HighLow").format(username, Followers,Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "HighLow").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
                elif PostsConv > 30 and PostsConv <= 100:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "HighMid").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "HighMid").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
                elif PostsConv > 100:
                    Hypo = Language.Translation.Translate_Language(
                        filename, "Report", "Specific", "HighHigh").format(username, Followers, Posts)
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Specific", "HighHigh").format(
                        Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + Followers + Font.Color.WHITE, Font.Color.GREEN + Posts + Font.Color.WHITE))
        else:
            Hypo = Language.Translation.Translate_Language(
                filename, "Report", "Specific", "Blocked")
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Report", "Specific", "Blocked"))
        try:
            f = open(report, "a")
            f.write("\n\n" + Hypo)
            f.close()
        except Exception as e:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ERROR: {}".format(str(e)))

    @staticmethod
    def Printer(username, found, Count, Percent, subject, Tags, InstagramParams, TwitterParamas, ScraperSites, ScrapeOp, PostLocations, PostGpsCoordinates):
        report = "GUI/Reports/Usernames/{}/Recap.txt".format(username)
        print(Font.Color.GREEN +
              "\n[+]" + Font.Color.WHITE + "GENERATING SUMMARY REPORT...")
        sleep(3)
        Total = round(Percent, 1)
        Percentual = Language.Translation.Translate_Language(
            filename, "Report", "Recap", "Summary").format(username, str(found), str(Count), username, str(Total) + "%")
        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
            filename, "Report", "Recap", "Summary").format(Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + str(found) + Font.Color.WHITE, Font.Color.GREEN + str(Count) + Font.Color.WHITE, Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + str(Total), "%" + Font.Color.WHITE))
        f = open(report, "w")
        f.write(
            "REPORT CREATED BY MR.HOLMES\n\nGENERATING SUMMARY REPORT...\n" + Percentual)
        f.close()
        if subject == "USERNAME":
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GENERATING TAGS REPORT...")
            sleep(3)
            Tag = Language.Translation.Translate_Language(
                filename, "Report", "Recap", "Tags").format(', '.join(Tags))
            print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Report", "Recap", "Tags").format(Font.Color.WHITE + "[" + Font.Color.GREEN + ', '.join(Tags) + Font.Color.WHITE + "]"))
            f = open(report, "a")
            f.write("\nGENERATING TAGS REPORT\n\n" + "[" + Tag + "]")
            f.close()
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GENERATING GENERAL HYPOTESY REPORT...")
            sleep(3)
            if Total < 10:
                General = Language.Translation.Translate_Language(
                    filename, "Report", "Recap", "Percentual_Low").format(username, str(Total))
                print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Recap",
                      "Percentual_Low").format(Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + str(Total) + Font.Color.WHITE))
            elif Total > 10 and Total < 20:
                General = Language.Translation.Translate_Language(
                    filename, "Report", "Recap", "Percentual_Mid").format(username, str(Total))
                print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Recap",
                      "Percentual_Mid").format(Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + str(Total) + Font.Color.WHITE))
            else:
                General = Language.Translation.Translate_Language(
                    filename, "Report", "Recap", "Percentual_High").format(username, str(Total))
                print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Report", "Recap",
                      "Percentual_High").format(Font.Color.GREEN + username + Font.Color.WHITE, Font.Color.GREEN + str(Total) + Font.Color.WHITE))

            f = open(report, "a+")
            f.write("\n\nGENERATING GENERAL HYPOTESY REPORT...\n\n" + General)
            f.close()

            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  "GENERATING HYPOTESYS ON VARIOUS SOCIAL MEDIAS")
            if ScrapeOp == "Positive":
                if "Instagram" in ScraperSites:
                    print(Font.Color.GREEN +
                        "\n[+]" + Font.Color.WHITE + "INSTAGRAM HYPOTESIS...")
                    Stats.Hypotesys(InstagramParams, username, report)
                if "Twitter" in ScraperSites:
                    print(Font.Color.GREEN +
                        "\n[+]" + Font.Color.WHITE + "TWITTER HYPOTESIS...")
                    Stats.Hypotesys(TwitterParamas, username, report)
            else:
                pass
        Encoding.Encoder.Encode(report)
