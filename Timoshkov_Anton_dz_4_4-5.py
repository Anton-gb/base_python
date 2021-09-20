import utils
import sys

if len(sys.argv) > 1:
    print(utils.currency_rates(sys.argv[1]))
else:
    print(utils.currency_rates('Usd'))
    print(utils.currency_rates('Usp'))
    print(utils.currency_rates('eUr'))
