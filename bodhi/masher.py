import fedmsg.consumers

from pprint import pprint

class Masher(fedmsg.consumers.FedmsgConsumer):
    """The Bodhi Masher.

    A fedmsg consumer that listens for messages from releng members.

    An updates "push" consists of::

    - verify that the message was sent by someone in releng
    - Lock repo
      - track which repos were completed
      - track which packages are in the push
    - Move builds
    - Update security bug titles
    - Expire buildroot overrides
    - Remove pending tags
    - mash
    - request_complete
    - Add testing updates to updates-testing digest
    - Generate/update updateinfo.xml and inject it into the repodata
    - Sanity check the repo
    - Flip the symlinks to the new repo
    - Cache the lateset repodata
    - Wait for the repo to hit the master mirror
    - Update bugzillas
    - Add comments to updates
    - Generate and email stable update notices
    - Email updates-testing digest
    - Unlock repo
    - Send fedmsgs

    """
    topic = 'org.fedoraproject.prod.bodhi.masher.*'
    config_key = 'masher'

    def __init__(self, *args, **kw):
        super(Masher, self).__init__(*args, **kw)

    def consume(self, msg):
        pprint(msg)

        # TODO: verify that this message was signed by releng
