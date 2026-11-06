
import cv2
import numpy as np

from effects.blur import GlowEffect
from effects.aura import AuraEffect
from effects.particles import ParticleEffect
from effects.portal import PortalEffect
from effects.lightning import LightningEffect

WIDTH, HEIGHT = 1280, 720

frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

glow = GlowEffect()
aura = AuraEffect()
particles = ParticleEffect()
portal = PortalEffect()
lightning = LightningEffect()

while True:

    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    point = (640, 360)

    # Purple aura
    aura.apply(frame, point)

    # Floating particles
    particles.emit(point, count=2)
    particles.update(frame)

    # Portal
    portal.apply(frame, (640, 360))

    # Lightning
    lightning.apply(frame, (400, 300), (850, 400))

    cv2.imshow("AI Magic Drawing - Effects", frame)

    key = cv2.waitKey(30) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()
