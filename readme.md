# open-door unsubscribe vulnerability 

Many websites offer the ability to "unsubscribe" from marketing emails. Some companies put these behind login-walls or offer unsubscribe links at the bottom of the marketing emails. Other companies, such as Uber, provide a publicly accessible unsubscribe page. https://www.uber.com/unsubscribe/

Uber uses a form with text input---making it very easy for customers to unsubscribe from "non-transactional" emails. Unfortunately, this also makes it very easy to auto-populate the form with guessed email addresses. For example, it would not be hard to use a list of likely userNames (https://github.com/insidetrust/statistically-likely-usernames) and drive a chrome browser to unsubscribe each of these email addresses in turn. This is done in the uber.py POC

Fortunately, Uber does have some security measures in place (i.e., after several loops, IP is blocked ==> "Something went wrong; please try again" instead of "Your subscription preferences have been updated") though these may be averted by randomizing IP addresses or other simple workarounds.  

## potential solution

A better solution might be to put the unsubscribe option behind a login wall, similar to how Ebay or Netflix handles unsubscribe requests.

## open questions
- Uber unsubscribe does not generate an email signaling the user of the unsubscribe action

## resources
- https://hackerone.com/reports/201314
  - Here, Uber does not confirm a successful removal---enumeration attack. I originally thought of this bug on Frys.com's unsubscribe page which does indicate users' email addresses, but it seems this vulnerability is not unheard of and may be found in various places
- https://www.frys.com/workflow/AcctMaint/fryspromocom/unsubc.jsp?site=cemail061416
  - Not only can we ubsubscribe a user, but we can learn the email addresses of users (if unsubscribe successful)
  
  
  
  