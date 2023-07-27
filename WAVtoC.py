import argparse, csv, os, ctypes

if __name__ == "__main__":
  parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
  parser.add_argument("--wavfile", help="WAV file input")
  parser.add_argument("--cfile", help="C file output")
  args = parser.parse_args()
  WaveformFile = args.wavfile
  Cfilename = args.cfile
  WAVfilePosition = 44

  if args.wavfile:
    if args.cfile:
      WAVfileSize = os.path.getsize(WaveformFile)
      WAVbuffer = (ctypes.c_byte * WAVfileSize)()
      WAVfile = open(WaveformFile, 'rb')
      WAVbuffer = WAVfile.read(WAVfileSize)
      WAVfile.close()

      if WAVbuffer[0] == 0x52 and WAVbuffer[1] == 0x49 and WAVbuffer[2] == 0x46 and WAVbuffer[3] == 0x46 and WAVbuffer[8] == 0x57 and WAVbuffer[9] == 0x41 and WAVbuffer[10] == 0x56 and WAVbuffer[11] == 0x45:
        if WAVbuffer[34] == 16:
          if WAVbuffer[22] == 1:
            with open(Cfilename, 'w', newline='') as csvfile:
              WAVwriter = csv.writer(csvfile, delimiter='*',quotechar='|', quoting=csv.QUOTE_NONE)

              # write the start row
              WAVwriter.writerow(['const word Waveform['] + [int((WAVfileSize - WAVfilePosition) / 2)] + ['] = {'])

              # write full rows
              while True:
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 22)]) + (WAVbuffer[(WAVfilePosition + 23)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 24)]) + (WAVbuffer[(WAVfilePosition + 25)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 26)]) + (WAVbuffer[(WAVfilePosition + 27)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 28)]) + (WAVbuffer[(WAVfilePosition + 29)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 30)]) + (WAVbuffer[(WAVfilePosition + 31)] << 8))] + [', '])
                WAVfilePosition += 32
                if ((WAVfileSize - WAVfilePosition) <= 32):
                  break

              # now write the last row which is partial
              if ((WAVfileSize - WAVfilePosition) == 2):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 4):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 6):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 8):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 10):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 12):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 14):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 16):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 18):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 20):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 22):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 24):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 22)]) + (WAVbuffer[(WAVfilePosition + 23)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 26):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 22)]) + (WAVbuffer[(WAVfilePosition + 23)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 24)]) + (WAVbuffer[(WAVfilePosition + 25)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 28):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 22)]) + (WAVbuffer[(WAVfilePosition + 23)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 24)]) + (WAVbuffer[(WAVfilePosition + 25)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 26)]) + (WAVbuffer[(WAVfilePosition + 27)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 30):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 22)]) + (WAVbuffer[(WAVfilePosition + 23)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 24)]) + (WAVbuffer[(WAVfilePosition + 25)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 26)]) + (WAVbuffer[(WAVfilePosition + 27)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 28)]) + (WAVbuffer[(WAVfilePosition + 29)] << 8))])
              elif ((WAVfileSize - WAVfilePosition) == 32):
                WAVwriter.writerow([hex((WAVbuffer[WAVfilePosition]) + (WAVbuffer[(WAVfilePosition + 1)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 2)]) + (WAVbuffer[(WAVfilePosition + 3)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 4)]) + (WAVbuffer[(WAVfilePosition + 5)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 6)]) + (WAVbuffer[(WAVfilePosition + 7)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 8)]) + (WAVbuffer[(WAVfilePosition + 9)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 10)]) + (WAVbuffer[(WAVfilePosition + 11)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 12)]) + (WAVbuffer[(WAVfilePosition + 13)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 14)]) + (WAVbuffer[(WAVfilePosition + 15)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 16)]) + (WAVbuffer[(WAVfilePosition + 17)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 18)]) + (WAVbuffer[(WAVfilePosition + 19)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 20)]) + (WAVbuffer[(WAVfilePosition + 21)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 22)]) + (WAVbuffer[(WAVfilePosition + 23)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 24)]) + (WAVbuffer[(WAVfilePosition + 25)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 26)]) + (WAVbuffer[(WAVfilePosition + 27)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 28)]) + (WAVbuffer[(WAVfilePosition + 29)] << 8))] + [', '] + [hex((WAVbuffer[(WAVfilePosition + 30)]) + (WAVbuffer[(WAVfilePosition + 31)] << 8))])

              # terminate it
              WAVwriter.writerow(['};'])

            # remove the unwanted delimiter characters
            CfileSize = os.path.getsize(Cfilename)
            CfileBuffer_origin = (ctypes.c_byte * CfileSize)()
            Cfile_origin = open(Cfilename, 'rb')
            CfileBuffer_origin = Cfile_origin.read(CfileSize)
            Cfile_origin.close()
            DelimiterByteCount = 0
            for ByteToCheck in range (CfileSize):
              if CfileBuffer_origin[ByteToCheck] == 0x2A:
                DelimiterByteCount += 1
            CfileBuffer_destination = (ctypes.c_byte * (CfileSize - DelimiterByteCount))()
            DelimiterByteCount = 0
            for ByteToTransfer in range (CfileSize):
              if CfileBuffer_origin[ByteToTransfer] != 0x2A:
                CfileBuffer_destination[(ByteToTransfer - DelimiterByteCount)] = CfileBuffer_origin[ByteToTransfer]
              else:
                DelimiterByteCount += 1
            Cfile_destination = open(Cfilename, 'wb')
            Cfile_destination.write(CfileBuffer_destination)
            Cfile_destination.close()       
            print("C file write complete")
          else:
            print("ERROR: Input file WAV format is not mono")
        else:
          print("ERROR: Input file WAV format is not 16 bit")
      else:
        print("ERROR: Input file is not WAV format")
    else:
      print("ERROR: C output file not specified")
  else:
    print("ERROR: Waveform input file not specified")