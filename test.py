from email.message import EmailMessage
import ssl
import smtplib


def send_email(email, name, phone_number, datetime_start, branch):
    message = 'Bai boschetarule plateste-ti ratele ca bag camatarii pe tine'
    bcr_email = 'bcr.cel.adevarat@gmail.com'
    bcr_password = 'asuqubtztnifhobm'

    em = EmailMessage()
    em['From'] = bcr_email
    em['To'] = email
    em.set_content(message)
    em.add_alternative("""
  <!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:v="urn:schemas-microsoft-com:vml" lang="en">

<head>
    <link rel="stylesheet" type="text/css" hs-webfonts="true"
          href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
    <title>Email template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Montserrat:wght@500;900&family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <meta property="og:title" content="Email template">

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style type="text/css">
        body {
            font-family: 'Inter';
        }
        a {
            text-decoration: underline;
            color: inherit;
            font-weight: bold;
            color: #253342;
        }

        h1 {
            font-size: 56px;
        }

        h2 {
            font-size: 28px;
            font-weight: 900;
        }

        p {
            font-weight: 100;
            font-size: 20px;
        }

        td {
            vertical-align: top;
        }

        #email {
            margin: auto;
            width: 600px;
            background-color: white;
        }

        button {
            font: inherit;
            background-color: #FF7A59;
            border: none;
            padding: 10px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 900;
            color: white;
            border-radius: 5px;
            box-shadow: 3px 3px #d94c53;
        }

        .subtle-link {
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #CBD6E2;
        }
        .bold {
            font-weight: bold;
        }
        .Description {
            font-size: 20px;
        }
        .colorBlue {
            color: #1A67D2;
        }
    </style>

</head>

<body
      style="width: 100%; margin: auto 0; padding:0; font-family:Lato, sans-serif; font-size:18px; color:#33475B; word-break:break-word; background-color: black;">

<div id="email">

    <table role="presentation" width="100%" align="center" style="margin-bottom: 15px">
        <tr>
            <td align="center" style="color: white;">
                <a href="www.bcr.ro" target="_blank"><img alt="Logo BCR" src="BCR.svg" align="middle"></a>
            </td>
        </tr>
        <tr>
            <td  align="center" style="color: white;">
                <img alt="Programare-vizita" src="BCR.png" width="450px"  align="middle" style="padding: 30px 30px 30px 30px;border-radius: 50px 50px 0px 0px;">
<!--                <h2 style="position:absolute;color:white;top: 150px; right: 770px; font-weight: bold;">Programarea<br>ta la BCR!</h2>-->
            </td>
        </tr>
    </table>

    <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 50px 50px 50px 80px;">
        <tr>
            <td>
                <p>Salut {Nume},</p>
                <p style="margin-top: 30px; margin-bottom: 30px;">
                    Programarea ta la  <span class="bold">{sucursala}</span> este confirmata.
                </p>
                <p class="bold" style="margin-bottom: 30px;">Detalii programare:</p>
                <p>Scopul vizitei:  <span class="bold">{scop}</span></p>
                <p>Locatie: <span class="bold">{locatie} </span></p>
                <p>Data si interval orar: <span class="bold">{orar} </span></p>
                <p>Adresa: <span class="bold">{adresa}</span></p>
            </td>
        </tr>
    </table>

    <table role="presentation" border="0" cellpadding="0" width="100%" align="center" style="margin-bottom: 15px;">
        <tr>
            <td align="center">
                <img alt="Programare-vizita" src="Bitmap.png" width="450px" style="padding: 30px 30px 30px 30px;">
            </td>
        </tr>
        <tr>
            <td style="padding: 50px 50px 50px 80px;">
                <a href="#" style="color: #1A67D2;text-decoration: none;font-weight: bold; font-size:20px;"><i class="fa-solid fa-location-arrow"></i>&nbsp&nbsp&nbsp&nbspAfiseaza traseul pe harta</a>
            </td>
        </tr>
    </table>

    <table role="presentation" border="0" border="0" cellpadding="0" width="100%" align="center" style="margin-bottom: 15px;padding: 0px 50px 50px 80px;">
        <tr>
            <td>
                <p class="Description">Pana cand ne intalnim, poti descarca si adauga programarea in calendarul tau.</p>
            </td>
        </tr>
        <tr>
            <td>
                <a href="#" style="color: #1A67D2; text-decoration: none;font-weight: bold; font-size:20px;"><i class="fa-regular fa-calendar"></i>&nbsp&nbsp&nbsp&nbspAdauga in calendar</a>
            </td>
        </tr>
    </table>
    <table role="presentation" border="0" border="0" cellpadding="0" width="100%" align="center" style="margin-bottom: 15px;padding: 0px 50px 50px 80px;">
        <tr>
            <td>
                <p class="Description">In cazul in care nu poti ajunge la data si intervalul orar stabilit, te rugam sa anulezi intalnirea.</p>
            </td>
        </tr>
        <tr>
            <td>
                <a href="#" style="color: #1A67D2; text-decoration: none;font-weight: bold; font-size:20px;"><i class="fa-solid fa-trash"></i>&nbsp&nbsp&nbsp&nbspAnuleaza vizita</a>
            </td>
        </tr>
    </table>

    <table role="presentation" border="0" border="0" cellpadding="0" width="100%" align="center" style="margin-bottom: 15px;padding: 0px 50px 50px 80px;">
        <tr>
            <td>
                <p class="Description">Pentru siguranta ta si a noastra, te rugam sa porti masca de protectie pe tot parcursul vizitei. Pe curand!</p>
                <p>Cu drag,<br>Echipa BCR</p>
            </td>
        </tr>
    </table>
    <table role="presentation" border="0" border="0" cellpadding="0" width="100%" align="center" style="margin-bottom: 15px">
        <tr>
            <td style="padding: 10px 120px 0px 120px;">
                <p class="Description" style="text-align: center; font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 20px;
line-height: 30px;

text-align: center;

color: #5C7999;">Acest mesaj a fost generat automat, te rugam
                    sa nu dai reply.
                    Pentru orice intrebare, scrie-ne un e-mail la <span class="colorBlue">contact.center@bcr.ro</span> sau suna-ne la <span class="colorBlue">*2227</span>.</p>
            </td>
        </tr>

    </table>

    <hr>

    <div style="margin: auto">
        <table role="presentation" style="margin: auto; width: 50%">
            <tr align="center">
                <td style="padding:10px; font-size: 40px; color: #5C7999;">
                    <a href="https://www.facebook.com/BCR.Romania" target="_blank"><i class="fa-brands fa-facebook"></i></a>
                </td>
                <td style="padding:10px; font-size: 40px;color: #5C7999;"><a href="https://twitter.com/infobcr" target="_blank"><i class="fa-brands fa-twitter"></i></a></td>
            <td>

                <td style="padding:10px; font-size: 40px;color: #5C7999;"><a href="https://www.instagram.com/georgepeinsta/?hl=ro" target="_blank"><i class="fa-brands fa-instagram"></i></a></td>

                <td style="padding:10px; font-size: 40px;color: #5C7999;">
                    <a href="https://www.youtube.com/@BancaComercialaRomana" target="_blank"><i class="fa-brands fa-youtube"></i></a>
                </td>
            </tr>
        </table>
    </div>
    <table>
        <tr>
            <td align="center">
                <p style="font-family: 'Inter';
font-style: normal;
font-weight: 600;
font-size: 17px;
line-height: 18px;
/* or 180% */

text-align: center;

color: #21416C;">Banca Comerciala Romana</p>
                <p style="font-size: 15px; padding: 0px 30px 0px 30px; color:#5C7999;">Business Garden, Calea Plevnei 159, Sector 6, Bucuresti, Cod postal 060013, Romania</p>
            </td>
        </tr>
    </table>
    <table role="presentation" width="100%" align="center" style="margin-bottom: 40px">
        <tr>
            <td align="center" style="color: white;">
                <a href="www.bcr.ro" target="_blank"><img alt="Logo BCR" src="BCR.svg" align="middle"></a>
            </td>
        </tr>
    </table>
    <br>

</div>
</body>

</html>
  """, subtype='html')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(bcr_email, bcr_password)
        smtp.sendmail(bcr_email, email, em.as_string())

send_email('clau_123@yahoo.com', 'claudiu', '0812e12', 'azi', 'bucuresti')