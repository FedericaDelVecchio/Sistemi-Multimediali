# Federica Del Vecchio, N46004430
# importo delle librerie necessarie
import cv2 as cv
import numpy as np
import datetime as dt
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# necessario per rimuovere il background, rispetto alla persona in primo piano
segmentor = SelfiSegmentation()

# stampa di cornici 'divertenti' che si possono applicare sulle immagini;
# prima le immagini devono essere lette e le informazioni devono essere salvate in delle variabili,
# IMREAD_UNCHANGED permette di conservare le informazioni riguardanti la trasparenza
frame1 = cv.imread("cornice_1.png", cv.IMREAD_UNCHANGED)
frame2 = cv.imread("cornice_2.png", cv.IMREAD_UNCHANGED)
frame3 = cv.imread("cornice_3.png", cv.IMREAD_UNCHANGED)
frame4 = cv.imread("cornice_4.png", cv.IMREAD_UNCHANGED)
frame5 = cv.imread("cornice_5.png", cv.IMREAD_UNCHANGED)
frame6 = cv.imread("cornice_6.png", cv.IMREAD_UNCHANGED)
# per poter visualizzare tutte le cornici nella stessa finestra, è necessario concatenarle,
# axis=1 specifica una concatenazione orizzontale, axis=0 quella verticale
temp_1 = np.concatenate((frame1, frame2), axis=1)
temp_2 = np.concatenate((temp_1, frame3), axis=1)
temp_3 = np.concatenate((frame4, frame5), axis=1)
temp_4 = np.concatenate((temp_3, frame6), axis=1)
frames = np.concatenate((temp_2, temp_4), axis=0)

# stampa di una stringa nel terminale
print("Vuoi scattare delle fotografie divertenti o delle fototessere?\nInserisci 0 nel primo caso, altrimenti 1: ")
# inserimento da tastiera della scelta presa
choice = int(input())
# finché non si inserisce 0 oppure 1, il processo non va avanti
while choice != 0 and choice != 1:
    choice = int(input())
if choice == 0:
    print("Inserisci il numero corrispondente alla cornice che si vuole selezionare: ")
    # apertura di una finestra chiamata 'Cornici (1 - 2 - 3, 4 - 5 - 6)' per poter visualizzare le cornici
    cv.imshow("Cornici (1 - 2 - 3, 4 - 5 - 6)", frames)
    # la window deve rimanere aperta per un certo intervallo di tempo
    cv.waitKey(50)
    # inserimento dell'intero associato alla cornice desiderata
    frame_number = int(input())
    while frame_number < 1 and frame_number > 6:
        frame_number = int(input())
    # subito dopo l'input, chiusura da programma della finestra specificata
    cv.destroyWindow("Cornici (1 - 2 - 3, 4 - 5 - 6)")

# creazione di un oggetto chiamato camera, di tipo OpenCV video capture,
# con 0 viene presa la prima delle telecamere connesse al computer
camera = cv.VideoCapture(1)
print("\nApertura delle cabina.")

# inizializzazione del contatore delle immagini
image_counter = 0

print("Per scattare le foto premi SPACE, per ricominciare premi ESC.")
# loop infinito a meno che non si incontri l'istruzione 'break'
while True:
    # la funzione read() di OpenCV legge i valori dall'oggetto 'camera' e restituisce due valori da memorizzare
    return_value, frame = camera.read()

    # controllo che la videocamera si sia aperta correttamente
    if not return_value:
        print("Si e' presentato qualche errore, ad esempio la  webcam non disponibile")
        exit(1)

    # solo nel caso in cui si e' scelto di scattare fototessere...
    if choice == 1:
        # rimozione dello sfondo e sostituzione di esso col colore bianco, (255, 255, 255)
        frame = segmentor.removeBG(frame, (255, 255, 255), threshold=0.35)
        # con soglia=1 viene rimorsa l'intera persona in foreground

    # il colorspace è BGR ovvero quello di default
    # conversione dello spazio di colore in modo tale che anche 'frame' presenti l'alpha channel,
    # ciò è necessario per poter applicare successivamente la funzione addWeighted
    frame = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    # tutti i valori di questo canale aggiuntivo sono posti a 1 dato che la foto è completamente opaca
    frame[:, :, 3] = 1

    # apertura di 'grid.png'
    grid = cv.imread("griglia.png", cv.IMREAD_UNCHANGED)
    # sovrapposizione di una griglia indicativa sulla finestra di cattura attraverso una funzione di blending;
    # tale grid mostra dove vengono tagliate le immagini e dove, piu' interamente, non viene applicato il blur o si aggiunge una cornice
    # addWeighted fa il merge; durante lo scatto, si visualizza la seguente immagine istante per istante
    to_print = cv.addWeighted(frame, 0.7, grid, 1, 0)

    # stampa nella window 'Cabina Fotografica'
    cv.imshow("Cabina fotografica", to_print)
    # visualizzazione della finestra per un solo millisecondo o finche' non viene premuto un tasto
    k = cv.waitKey(1)

    # uscita dal while dopo aver catturato 4 immagini
    if image_counter == 4:
        print("Chiusura della cabina.\n")
        break
    # se viene premuto il tasto ESC, si ricomincia dall'inizio lo scatto delle foto
    elif k % 256 == 27:
        image_counter = 0
        print("Ricomincia a scattare!")
    # in corrispondenza della pressione del tasto SPACE si scatta un fotografia
    elif k % 256 == 32:
        # incremento di uno del contatore
        image_counter += 1
        # il nome dell'immagine varia ogni volta e dipende dal valore di image_counter
        image_name = "fotografia_{}.png".format(image_counter) # image_name è una stringa
        # creazione e scrittura del file image_name.png
        cv.imwrite(image_name, frame)
        print("La fotografia {} e' stata appena scattata!".format(image_counter))
#fine del while

# chiusura del video stream dalla fotocamera
camera.release()
# chiusura di tutte le finestre aperte al momento
cv.destroyAllWindows()

img1 = cv.imread("fotografia_1.png")
img2 = cv.imread("fotografia_2.png")
img3 = cv.imread("fotografia_3.png")
img4 = cv.imread("fotografia_4.png")
# nel caso in cui si desidera stampare foto per una patente o un passaporto queste devono essere tutte uguali,
# selezione della preferita tra le quattro fotografie scattate
if choice == 1:
    print("Segli la tua foto preferita tra le 4 che sono state scattate: ")
    img_temp_1 = np.concatenate((img1, img2), axis=1)
    img_temp_2 = np.concatenate((img3, img4), axis=1)
    img_temp_3 = np.concatenate((img_temp_1, img_temp_2), axis=0)
    cv.imshow("Foto (1 - 2 , 3 - 4)", img_temp_3)
    cv.waitKey(50)

    number = int(input())
    while number != 1 and number != 2 and number != 3 and number != 4:
        number = int(input())
    cv.destroyWindow("Foto (1 - 2 , 3 - 4)")

    if number == 1:
        img2 = img1
        img3 = img1
        img4 = img1
    elif number == 2:
        img1 = img2
        img3 = img2
        img4 = img2
    elif number == 3:
        img1 = img3
        img2 = img3
        img4 = img3
    elif number == 4:
        img1 = img4
        img2 = img4
        img3 = img4

# applicando una correzione gamma è possibile cambiare la luminosità dell'immagine
print("Inserisci il valore di gamma per poter fare la gamma correction,\n"
      "(se gamma<1 l'immagine sara' piu' chiara, se gamma>1 piu' scura, se gamma=1 non vi è differenza): ")
# stampa, ad esempio, della prima immagine per poter valutare che valore di gamma inserire da tastiera
cv.imshow("Determina di quanto diminuire o aumentare la luminosita'.", img1)
cv.waitKey(50)
gamma = float(input())
cv.destroyWindow("Determina di quanto diminuire o aumentare la luminosita'.")
# creazione della look up table
values = np.arange(0, 256)
lut = np.uint8(255 * np.power((values/255.0), gamma))

cv.imwrite("fotografia_1.png", img1)
cv.imwrite("fotografia_2.png", img2)
cv.imwrite("fotografia_3.png", img3)
cv.imwrite("fotografia_4.png", img4)

print("\nInizio dell'elaborazione delle immagini...")
for i in range(4):
    # creazione di image_temp per la lettura dell'immagine
    image_temp = cv.imread("fotografia_{}.png".format(i+1))
    # ritaglio di 'image_temp' nel formato di una fototessera
    crop_img = image_temp[40:440, 160:480]

    # gamma correction; la funzione LUT permette di applicare una lookup table transform
    gamma_img = cv.LUT(crop_img, lut)

    img = cv.cvtColor(gamma_img, cv.COLOR_BGR2BGRA)
    img[:, :, 3] = 1

    # nel caso delle foto 'divertenti'...
    if choice == 0:
        # creazione di un array di zero della stessa dimensione e tipo di img
        shapes = np.zeros_like(img, np.uint8)
        # memorizzazione delle dimensioni dei filtri in delle variabili
        h, w = frame1.shape[:2]
        if frame_number == 1:
            shapes[img.shape[0]-h:, img.shape[1]-w:] = frame1
            # creazione della maschera alpha
            mask = shapes.astype(bool)
        elif frame_number == 2:
            shapes[img.shape[0]-h:, img.shape[1]-w:] = frame2
            mask = shapes.astype(bool)
        elif frame_number == 3:
            shapes[img.shape[0]-h:, img.shape[1]-w:] = frame3
            mask = shapes.astype(bool)
        elif frame_number == 4:
            shapes[img.shape[0]-h:, img.shape[1]-w:] = frame4
            mask = shapes.astype(bool)
        elif frame_number == 5:
            shapes[img.shape[0]-h:, img.shape[1]-w:] = frame5
            mask = shapes.astype(bool)
        elif frame_number == 6:
            shapes[img.shape[0]-h:, img.shape[1]-w:] = frame6
            mask = shapes.astype(bool)
        img[mask] = cv.addWeighted(img, 0, shapes, 1, 0)[mask]
    # per le fototessere invece...
    else:
        # applicazione di un filtro Gaussiano ai bordi della foto;
        # memorizzazione delle informazioni che non devono essere alterate in una variabile temporanea,
        # queste corrispondono ai pixel più interni dell'immagine
        not_blurred_img = img[60:340, 60:260]
        # impiego del filtro passa-basso di sfocatura su tutto 'crop_img'
        img = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
        # ricopiatura opportuna di 'not_blurred_img' in 'blurred_img'
        img[60:340, 60:260] = not_blurred_img

    final_img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
    cv.imwrite("immagine_{}.png".format(i+1), final_img)
# fine del for

image_1 = cv.imread("immagine_1.png")
image_2 = cv.imread("immagine_2.png")
image_3 = cv.imread("immagine_3.png")
image_4 = cv.imread("immagine_4.png")

# creazione di bordi bianchi avvalendosi della funzione copyMakeBorder
image_1 = cv.copyMakeBorder(
    image_1, 25, 0, 25, 25, cv.BORDER_CONSTANT, value=[255, 255, 255])
image_2 = cv.copyMakeBorder(
    image_2, 25, 0, 0, 25, cv.BORDER_CONSTANT, value=[255, 255, 255])
image_3 = cv.copyMakeBorder(
    image_3, 25, 135, 25, 25, cv.BORDER_CONSTANT, value=[255, 255, 255])
image_4 = cv.copyMakeBorder(
    image_4, 25, 135, 0, 25, cv.BORDER_CONSTANT, value=[255, 255, 255])

img_top = np.concatenate((image_1, image_2), axis=1)
img_bottom = np.concatenate((image_3, image_4), axis=1)
image = np.concatenate((img_top, img_bottom), axis=0)

# prelievo della data e dell'orario attuale
date_ = str(dt.datetime.now())
# gli ultimi caratteri non sono rilevanti quindi vengono tagliati via
date = date_[:len(date_)-7]
# scrittura su 'image'
cv.putText(image, text=date, org=(20, 950), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1,
           color=(0, 0, 0), thickness=2, lineType=cv.LINE_AA)

# incolliamo un simbolo di 'ritaglia qui' su image
cut_here = cv.imread("taglia_qui.png")
# rotazione di 90 gradi in senso antiorario
cut_here = cv.rotate(cut_here, cv.ROTATE_90_COUNTERCLOCKWISE)
# flip verticale
cut_here = cv.flip(cut_here, 0)
# flip orizzontale
cut_here = cv.flip(cut_here, 1)
# ridimensionamento
cut_here = cv.resize(cut_here, (280, 100))
# sostituzione di una data parte di image con cut_here
image[850:950, 410:690] = cut_here
print("Fine dell'elaborazione delle immagini...")

print("Che nome vuoi dare al file che memorizza l'immagine finale? ")
name = input()
file_name = "{}.png".format(name)
print("Salvataggio...")
cv.imwrite(file_name, image)

immagine = cv.imread(file_name)
# la funzione getcwd restituisce il percorso attuale
path = os.getcwd()
print("L'immagine finale è memorizzata nel file PNG chiamato '", name, "' e il suo path e' ", path)
cv.imshow("Immagine finale!", immagine)
cv.waitKey(0)
cv.destroyAllWindows()
