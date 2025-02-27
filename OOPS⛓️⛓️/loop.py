
import sys
argv=["hello","world",407]
# sys.argv se arguments lete hain
# sys.argv[0] script ka naam hota hai, ise exclude karte hain
arguments = sys.argv[1:]

# Arguments ki count print karte hain
print(f"Total arguments: {len(arguments)}")