import markovify

# Large sample text to train the model, the more text the better the result
text = """
Once upon a time, in the protective corners of cyberspace, existed four guardian heroes named Exchange, SharePoint, OneDrive, and Teams. They were the embodiment of unity, wisdom, accuracy, and action, ensuring smooth, efficient, and secure communication throughout the digital kingdoms. Sadly, they would face countless battles against a notoriously cunning enemy - malicious threat actors who were always on the prowl, seeking to wreak havoc and disorder.

Exchange, the first hero, was the guardian of mail communications. He expertly managed and secured all email interactions, ensuring they were delivered promptly and safely. His prowess lay in arranging tight protocols and filters to shield the kingdom's messages from phishing attempts and other malicious intrusions. But behind his formidable defense also lay vulnerability, as the threat actors always eyed valuable data circulating through the emails.

SharePoint, the next hero, embodied collaborative might. He stood as the beacon of teamwork, allowing kingdoms to conveniently co-author and share documents within their secure fortress. Duplicity and confusion were his enemies, and he dispelled them with his powers, thereby enabling seamless collaboration. Still, the threat actors often attempted to corrupt his cooperative efforts, jeopardizing the files and projects stored within his realm.

Then, OneDrive, the reliable custodian of data, ensured that individual users could store, share, and sync their files across devices securely. He was a seamless blend of efficiency and stability. But, he knew that his realm was a juicy target for threat actors as it contained the kingdom's valuable data, and they would stop at nothing to gain illegal access.

Lastly, Teams, the hero of live interaction, took charge of the kingdom's real-time communication. He brought heroes, warriors, and common folk together in virtual halls for productive and secure discussions. Despite his crucial role, Teams was often haunted by the threat actors, who sowed seeds of disruption through uninvited infiltrations in these delicate interactions.

The coherence between these four heroes was their greatest weapon against the malicious threat actors. Each guardian possessed unique capabilities, complementing each other to structure a solid defense. Exchange would intercept spam messages, SharePoint streamlined collaboration to reduce vulnerabilities, OneDrive's backups could restore damaged or lost files, and Teams safeguarded private meetings.

But, one day, the malicious threat actors unleashed a massive synchronized attack on the kingdoms. They attempted to penetrate Exchange's email system, breach SharePoint's safe collaboration spaces, target sensitive files stored in OneDrive, and disrupt critical meetings happening in Teams. The heroes braced themselves for the grueling battle ahead.

Exchange strengthened his filters and built a wall of encryption, successfully blocking phishing emails. SharePoint utilized the power of versioning and stringent permission control, foiling the attempts to break into document libraries. OneDrive enabled multi-factor authentication, creating an intricate barrier that the threat actors found impossible to breach.

Teams, meanwhile, tightened the security controls on meetings and conversations, ensuring only authorized users had access. He deployed advanced threat protection mechanisms to detect and block suspicious activities. However, the villains were persistent and increased their attack intensity.

In the face of such relentless onslaught, these four heroes united their strengths. The combined force allowed them to counter the multifaceted threats effectively. Exchange and SharePoint worked on warding off the majority of the attacks while Teams and OneDrive focused on securing crucial data and interactions.

In the end, the heroes claimed victory, successfully repelling the coordinated assault by the malicious threat actors. This adventure reiterated the importance of Exchange, SharePoint, OneDrive, and Teams working together. Their joint efforts proved that unity, combined with distinctive abilities, is a potent recipe to thwart even the most dangerous threats in the expansive kingdom of cyberspace."""

# Build the model
text_model = markovify.Text(text)

def chatbot_response():
    # Generate a sentence
    return text_model.make_sentence()