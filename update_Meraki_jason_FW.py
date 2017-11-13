import argparse
import sys
import json


MERAKI_JSON_FILE = "MerakiMXL3Rules.json"


def _save_meraki_json(meraki_json):
    with open(MERAKI_JSON_FILE, 'w+') as f:
        f.write(json.dumps(meraki_json, indent=2, sort_keys=True))


def add_rule(new_comment, new_dest_cidr):

    new_rule = {
      "comment": new_comment,
      "policy": "deny",
      "protocol": "any",
      "srcPort": "Any",
      "srcCidr": "Any",
      "destPort": "Any",
      "destCidr": new_dest_cidr,
      "syslogEnabled": False
    }

    with open(MERAKI_JSON_FILE, 'r') as f:
        meraki_json = json.load(f)

    old_rules = meraki_json['rules']
    new_rules = [new_rule] + old_rules
    meraki_json['rules'] = new_rules

    _save_meraki_json(meraki_json)


def ask_add_rule():
    new_comment = raw_input("New Comment for new rule:\n")
    new_cidr = raw_input("New destCidr for new rule:\n")
    add_rule(new_comment, new_cidr)


def update_rule(rule):
    for el in ['comment', 'destCidr']:
        print "Current %s" % el
        print rule[el]
        new_el = raw_input('New %s (blank to ignore):\n' % el)
        if new_el.strip() != "":
            rule[el] = new_el
    return rule


def ask_update_rule():
    # f = open(MERAKI_JSON_FILE, 'r')
    # meraki_json = json.load(f)
    # f.close()

    with open(MERAKI_JSON_FILE, 'r') as f:
        meraki_json = json.load(f)

    # Only update one of the first rules, before the uDevice rules
    for rule_index in range(len(meraki_json['rules'])):
        rule = meraki_json['rules'][rule_index]
        curr_comment = rule['comment']
        if curr_comment.startswith('uDevice'):
            # Encountered uDevice rules. Not going to change any below that rule
            print "Encountered uDevice rules. Quitting"
            break
        print json.dumps(rule, indent=2, sort_keys=True)
        update_answer = 'n'
        update_answer = raw_input('Update this rule (y/N)? ')
        if update_answer.lower().startswith('y'):
            new_rule = update_rule(rule)
            print 
            print "Adding rule:"
            print json.dumps(rule, indent=2, sort_keys=True)
            print
            meraki_json['rules'][rule_index] = new_rule
            print "Continuing with other rules..."

    _save_meraki_json(meraki_json)


if __name__ == "__main__":

    class HelpDefaultParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    argparser = HelpDefaultParser()
    argparser.add_argument('--add-rule', action='store_true', help="Add a rule to the current Meraki Ruleset")
    argparser.add_argument('--update-rule', action='store_true', help="Update an existing rule in the current Meraki Ruleset")
    parsed_args = argparser.parse_args(sys.argv[1:])

    if parsed_args.add_rule:
        ask_add_rule()
    elif parsed_args.update_rule:
        ask_update_rule()
