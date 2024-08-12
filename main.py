import pasteboard
import pandoc
import os

pb = pasteboard.Pasteboard()
# print(pb.get_contents(type=pasteboard.String))

pd = pandoc.read(pb.get_contents())
# print(pd)

pandoc.write(pd,"temp.rtf")
with open("temp.rtf","r") as f:
    rtf = f.read()

os.remove("temp.rtf")

rtf = '{\\rtf1\n' + rtf + '\n}\n'
# print(rtf)

pb.set_contents(rtf, type=pasteboard.RTF)