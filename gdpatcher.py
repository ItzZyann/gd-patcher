# FREE TO COPY THE CODE
# AS LONG AS YOU CREDITED ME
# @ItzZyann

import os

def patch_file(input_path, output_path, patches):
 with open(input_path, 'r+b') as f:
 data = f.read()
    
 with open(output_path, 'w+b') as f:
  f.write(data)
        
 for address, patch in patches:
  f.seek(address)
  f.write(patch.decode('hex'))

def main():
 print("\033[96mWelcome to GD Patcher\033[0m")
    
 # Check if libcocos2dcpp.so exists in lib32 folder
 # because yes lol.
 input_path = "lib32/libcocos2dcpp.so"
 output_path = "patched/libcocos2dcpp.so"
    
 if not os.path.exists(input_path):
  print("\033[91mError: libcocos2dcpp.so not found in lib32 folder.\033[0m")
  return
 
 # From my GDSH
 # Geometry Dash Safe Hacks
 patches = {
  1: [(0x00308d20, "7047")],
  2: [(0x004057e0, "0120"), (0x004057e2, "7047")],
  3: [(0x00319fb4, "0120"), (0x00319fb6, "7047")],
  4: [(0x0031a1a0, "0120"), (0x0031a1a2, "7047")],
  5: [(0x002b45aa, "0120")],
 }

 # The messages
 # because yes?
 # Damn, I feel nostalgic when
 # I make / code using python.
    
 print("\033[92m1. Noclip\033[0m")
 print("\033[92m2. Unlock All\033[0m")
 print("\033[92m3. Unlock Icon\033[0m")
 print("\033[92m4. Unlock Color\033[0m")
 print("\033[92m5. Show Controls\033[0m")
 print("\033[92mType 'exit' to apply patches and quit\033[0m")

 accumulated_patches = []

 while True:
  patch_choice = raw_input("\033[93mEnter the number you want to patch: \033[0m")
        
 if patch_choice.lower() == "exit":
  if accumulated_patches:
   all_patches = [patch for sublist in accumulated_patches for patch in sublist]
   patch_file(input_path, output_path, all_patches)
   
   print("\033[92mPatches applied for 32-bit (armeabi-v7a). Patched file saved to patched/libcocos2dcpp.so\033[0m")
  else:
   print("\033[91mNo patches were applied.\033[0m")
   break

 # This took me 20+ minutes
 # figuring out how to do
 # multi patches.
 
 try:
  patch_choice = int(patch_choice)
  
  except ValueError:
   print("\033[91mInvalid input. Please enter a number between 1 and 5, or type 'exit' to quit.\033[0m")
   continue

  if patch_choice in patches:
   accumulated_patches.append(patches[patch_choice])
   print("\033[92mPatch queued. You can add more patches or type 'exit' to apply them.\033[0m")
  else:
   print("\033[91mInvalid choice. Please enter a number between 1 and 5.\033[0m")

if __name__ == "__main__":
 main()