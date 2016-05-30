# xlr-slack-plugin

This plugin provides a notification task to send Slack messages to channels or direct messages.
It's based on Incoming Webhooks integration, which provides a URL within an authorization token ready to POST messages.

See [Slack Incoming Webhooks](https://api.slack.com/incoming-webhooks) documentation for background information on post messages from external sources into Slack.

## Slack server setup

Before to use Slack notification task, it's needed to setup a Slack server definition within the following information:

- **Title:** Name of the Slack server definition.
- **Slack URL:** Tokenized URL provided by the Incoming WebHook integration.
- **User name:** Name to use in the notifications.
- **User icon:** Icon to use in the notifications, it should be a icon emoji, e.g. `:ghost:`.
- **Proxy URL:** Proxy URL to use in format `http://username:password@proxyurl:proxyport`, leave it in blank if isn't required.

## Notification task

The Slack notification task needs the next information:

- **Server:** The Slack server definition to use.
- **Channel:** The target for the notification, use `#` or `@` to refer to a channel or direct message.
- **Message:** The notification message text, it could be [formatted](https://api.slack.com/docs/formatting).
