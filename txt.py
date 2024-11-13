import os

# Define las rutas a las carpetas de imágenes
train_images_folder = "D:\ESP_ MACHINE_LEARNING\MACHINE_LEARNING 2\Encuentro_final\DATA\Train\images"
val_images_folder = "D:\ESP_ MACHINE_LEARNING\MACHINE_LEARNING 2\Encuentro_final\DATA\Val\images"

# Define las rutas de salida para los archivos .txt
train_txt_path = "D:\ESP_ MACHINE_LEARNING\MACHINE_LEARNING 2\Encuentro_final\DATA\Train.txt"
val_txt_path = "D:\ESP_ MACHINE_LEARNING\MACHINE_LEARNING 2\Encuentro_final\DATA\Val.txt"

# Función para generar el archivo .txt con rutas correctas
def generate_txt_file(images_folder, txt_path):
    with open(txt_path, 'w') as f:
        # Itera sobre cada archivo en la carpeta de imágenes
        for img_name in os.listdir(images_folder):
            # Asegura que solo se agreguen archivos de imagen
            if img_name.lower().endswith(('.png', '.jpg', '.jpeg', 'jfif', 'webp')):
                img_path = os.path.join(images_folder, img_name).replace('\\', '/')
                f.write(img_path + '\n')

# Generar Train.txt y Val.txt
generate_txt_file(train_images_folder, train_txt_path)
generate_txt_file(val_images_folder, val_txt_path)

print("Archivos Train.txt y Val.txt generados correctamente.")


