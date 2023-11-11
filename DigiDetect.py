import sys
import phonenumbers as pn
from phonenumbers import carrier as c, timezone as tz, geocoder as gc
from colorama import Fore, Style

def print_colored(message, color=Fore.WHITE, style=Style.RESET_ALL, end='\n'):
    print(color + message + Style.RESET_ALL, end=end)

def get_phone_info(num):
    try:
        parsed_num = pn.parse(num, None)
        if pn.is_valid_number(parsed_num):
            country_code_color = Fore.CYAN
            general_info_color = Fore.GREEN
            error_color = Fore.RED

            # Phone number information
            print_colored("Phone number information:", country_code_color, Style.BRIGHT)

            # Country Code
            print_colored(f"\nCountry Code: ", country_code_color, Style.BRIGHT)
            print_colored(f"{parsed_num.country_code}", general_info_color, Style.BRIGHT)

            # National Number
            print_colored(f"\nNational Number: ", country_code_color, Style.BRIGHT)
            print_colored(f"{parsed_num.national_number}", general_info_color, Style.BRIGHT)

            # International Format
            print_colored(f"\nInternational Format: ", country_code_color, Style.BRIGHT)
            print_colored(f"{pn.format_number(parsed_num, pn.PhoneNumberFormat.INTERNATIONAL)}", general_info_color, Style.BRIGHT)

            # National Format
            print_colored(f"\nNational Format: ", country_code_color, Style.BRIGHT)
            print_colored(f"{pn.format_number(parsed_num, pn.PhoneNumberFormat.NATIONAL)}", general_info_color, Style.BRIGHT)

            region = gc.region_code_for_number(parsed_num)
            country = gc.description_for_number(parsed_num, "en", region)

            # Country Name
            print_colored(f"\nCountry Name: ", country_code_color, Style.BRIGHT)
            print_colored(f"{country}", general_info_color, Style.BRIGHT)

            # Carrier
            if pn.is_possible_number(parsed_num):
                carrier_info = c.name_for_number(parsed_num, "en")
                print_colored(f"\nCarrier: ", country_code_color, Style.BRIGHT)
                print_colored(f"{carrier_info}", general_info_color, Style.BRIGHT)
            else:
                print_colored("\nCarrier information not available for this number.", error_color + Style.BRIGHT)

            # Timezone
            time_zone_info = tz.time_zones_for_number(parsed_num)
            if time_zone_info:
                print_colored(f"\nTimezone: ", country_code_color, Style.BRIGHT)
                print_colored(f"{time_zone_info[0]}", general_info_color, Style.BRIGHT)
            else:
                print_colored("\nTimezone information not available for this number.", error_color + Style.BRIGHT)

            # Number Type
            print_colored(f"\nNumber Type: ", country_code_color, Style.BRIGHT)
            print_colored(f"{pn.number_type(parsed_num)}", general_info_color, Style.BRIGHT)

            # Geographical Area Description
            print_colored(f"\nGeographical Area Description: ", country_code_color, Style.BRIGHT)
            print_colored(f"{gc.description_for_number(parsed_num, 'en', region)}", general_info_color, Style.BRIGHT)

        else:
            print_colored("Invalid phone number.", error_color + Style.BRIGHT)
    except pn.NumberParseException as e:
        print_colored(f"Error: {e}", error_color + Style.BRIGHT)

if __name__ == "__main__":
    country_code_color = Fore.CYAN
    error_color = Fore.RED

    if len(sys.argv) != 2:
        print_colored("Usage: python3 DigiDetect.py +<phone_number>", error_color + Style.BRIGHT)
    else:
        phone_number = sys.argv[1]
        get_phone_info(phone_number)
