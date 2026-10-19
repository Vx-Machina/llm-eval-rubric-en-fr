# French (France) localisation checklist · Checklist de localisation fr-FR

Use this with criterion 4 (language & locale) and criterion 5 (register). Each item gives a typical fault and the natural fr-FR form.

## Typography · Typographie
- [ ] **Non-breaking space before `; : ! ?` and inside « guillemets »**: « Attention : danger ! » not "Attention: danger!"
- [ ] **French quotation marks** « … » rather than "…" (except in code).
- [ ] **Decimal comma, space as thousands separator**: 1 234,5 € not 1,234.5€. Currency symbol after the number, with a space.
- [ ] **Dates and times**: 19 octobre 2026, 14 h 30 or 14:30. Not "October 19th" or "2:30 PM".
- [ ] **Capitals**: months, days and languages are lower case (*lundi*, *octobre*, *le français*); headings don't capitalise every word.
- [ ] Accents kept on capitals where possible (*État*, *À noter*).

## Anglicisms and calques · Anglicismes et calques
| Typical in translated text | Natural fr-FR |
|---|---|
| « Je vais vous revenir » | « Je reviens vers vous » / « Je vous recontacte » |
| « Ça fait du sens » | « C'est logique » / « Ça a du sens » |
| « Adresser un problème » | « Traiter / résoudre un problème » |
| « Être en charge de » | « Être chargé de » / « Être responsable de » |
| « Opportunité » (for *occasion*) | « Occasion » |
| « Supporter un projet » | « Soutenir un projet » |
| « Définitivement » (for *definitely*) | « Sans aucun doute » / « Clairement » |
| « Éventuellement » (for *eventually*) | « Finalement » / « À terme » |
| « Basé sur » (overused) | « Fondé sur » / « D'après » / « À partir de » |

## Register · Registre
- [ ] *Vous* by default for an unknown user, customer support and professional contexts. *Tu* only if the prompt uses it, or for clearly casual or gaming contexts.
- [ ] Don't switch between *tu* and *vous* within one answer.
- [ ] Inclusive writing (*point médian*, e.g. « les utilisateur·rices ») only if the prompt or client style guide asks for it. Otherwise prefer neutral wording.

## Locale facts · Faits propres à la France
- [ ] Units: metric, °C, 24-hour clock.
- [ ] French institutions and usage when the user is in France: emergency number **112** (or 15 SAMU, 18 pompiers, 17 police); phone format 06 12 34 56 78 or +33 6 12 34 56 78.
- [ ] Don't import other locales' facts (US legal and tax rules, Québec vocabulary such as *courriel* is fine in France, but *char* for car is not).

## Internet and community language · Langue d'internet et des communautés
- [ ] Slang, abbreviations and memes (*mdr*, *ptdr*, *jsp*, *frère*) only when the context is casual. Check they're used correctly, not mixed with formal grammar.
- [ ] Code-switching EN↔FR is natural in gaming and tech communities (*« on a un bug sur le serveur »*), but not in formal answers.
