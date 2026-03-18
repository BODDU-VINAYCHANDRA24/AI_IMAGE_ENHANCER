import cv2
import torch
from realesrgan import RealESRGANer
from basicsr.archs.srvgg_arch import SRVGGNetCompact


def enhance_image(input_path, output_path, progress):


  # Decide whether to use GPU or CPU
    # If CUDA is available, it will speed up processing a lot
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    
    
    # Load model
    # Initialize the SRVGG model architecture used by Real-ESRGAN
    # These parameters define how the neural network is structured
    model = SRVGGNetCompact(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_conv=32,
        upscale=4,
        act_type='prelu'
    )

    # Use tiling to avoid memory crash
    upsampler = RealESRGANer(
        scale=4,
        model_path="models/realesr-general-x4v3.pth",
        model=model,
        tile=64,          # 🔥 prevents memory crash
        tile_pad=10,
        pre_pad=0,
        half=True if device.type == "cuda" else False,
        device=device
    )

    progress["value"] = 10

 # Read the input image using OpenCV
    img = cv2.imread(input_path)

    if img is None:
        raise Exception("Failed to read image")

    progress["value"] = 30


    # Resize large images to prevent memory crashes during processing

    h, w = img.shape[:2]
    if max(h, w) > 800:
        scale = 800 / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)))

    progress["value"] = 50

    print("Enhancement started...")

    # Perform the actual image enhancement
    output, _ = upsampler.enhance(img, outscale=2)

    print("Enhancement finished!")

    progress["value"] = 80

 # Save the enhanced image to output path
    cv2.imwrite(output_path, output)

    progress["value"] = 100