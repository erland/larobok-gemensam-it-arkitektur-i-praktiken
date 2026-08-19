# Teknisk standard: Identitets- och federationsprotokoll

## Syfte
Standardisera protokoll för autentisering, federation och delegerad åtkomst.

## Typ
Teknikstandard

## Relaterade förmågor
- Identitet och tillit
- Integration och kommunikation

## Standard
- OpenID Connect bör användas för modern användarautentisering där protokollet passar.
- OAuth 2.x bör användas för delegerad API-åtkomst.
- X.509-certifikat används för PKI-baserad teknisk tillit.
- mTLS kan användas för ömsesidig tjänsteautentisering där behovet motiverar det.
- SAML 2.0 kan användas där externa eller befintliga miljöer kräver det.

## Tokenformat
JWT kan användas där självbeskrivande tokens är lämpliga, men ska inte väljas enbart av vana.

## Avgränsning
Exakta flöden, algoritmer och profilkrav dokumenteras separat.
