from music21 import *
# Define the key, tempo, and time signature
key = key.Key('C')
tempo = tempo.MetronomeMark(number=120)
ts = meter.TimeSignature('4/4')
environment.UserSettings()['lilypondPath'] =  'C:/lilypond-2.24.0/bin/lilypond.exe'

# Create the main stream
main_stream = stream.Score()

# Create a stream for tubular bells
bells_stream = stream.Part()

# Set the instrument for the stream
bells_stream.insert(0, instrument.TubularBells())

# Define the notes for tubular bells
bells_notes = [note.Note("C4", quarterLength=1.0, volume=3.0),
               note.Note("D4", quarterLength=0.5, volume=3.0),
               note.Note("E4", quarterLength=0.5, volume=3.0),
               note.Note("F4", quarterLength=0.5, volume=3.0),
               note.Note("G4", quarterLength=0.5, volume=3.0),
               note.Note("A4", quarterLength=0.5, volume=3.0),
               note.Note("B4", quarterLength=0.5, volume=3.0),
               note.Note("C5", quarterLength=0.5, volume=3.0),
               note.Note("D5", quarterLength=0.5, volume=3.0),
               note.Note("E5", quarterLength=0.5, volume=3.0),
               note.Note("F5", quarterLength=0.5, volume=3.0),
               note.Note("G5", quarterLength=0.5, volume=3.0),
               note.Note("A5", quarterLength=0.5, volume=3.0),
               note.Note("B5", quarterLength=0.5, volume=3.0),
               note.Note("C6", quarterLength=0.5, volume=3.0),
               note.Note("D6", quarterLength=0.5, volume=3.0),
               note.Note("E6", quarterLength=0.5, volume=3.0),
               note.Note("F6", quarterLength=0.5, volume=3.0),
               note.Note("G6", quarterLength=0.5, volume=3.0),
               note.Note("A6", quarterLength=0.5, volume=3.0),
               note.Note("B6", quarterLength=0.5, volume=3.0),
               note.Note("C7", quarterLength=0.5, volume=3.0),
               note.Note("D7", quarterLength=0.5, volume=3.0),
               note.Note("E7", quarterLength=0.5, volume=3.0),
               note.Note("F7", quarterLength=0.5, volume=3.0),
               note.Note("G7", quarterLength=0.5, volume=3.0),
               note.Note("A7", quarterLength=0.5, volume=3.0),
               note.Note("B7", quarterLength=0.5, volume=3.0),
               note.Note("C8", quarterLength=0.5, volume=3.0),
               note.Note("D8", quarterLength=0.5, volume=3.0),
               note.Note("E8", quarterLength=0.5, volume=3.0),
               note.Note("F8", quarterLength=0.5, volume=3.0),
               note.Note("G8", quarterLength=0.5, volume=3.0),
               note.Note("A8", quarterLength=0.5, volume=3.0),
               note.Note("B8", quarterLength=0.5, volume=3.0)
               ]
# Add the notes to the tubular bells stream
bells_stream.append([note for note in bells_notes])

# Add the tubular bells stream to the main stream
main_stream.append(bells_stream)

# Add the key, tempo, and time signature to the main stream
main_stream.insert(0, key)
main_stream.insert(0, tempo)
main_stream.insert(0, ts)

# Play the main stream
main_stream.write('midi', 'mrImpulseoutro.mid')









environment.UserSettings()['lilypondPath'] =  'C:/lilypond-2.24.0/bin/lilypond.exe'
main_stream.write('lily.pdf', 'mrImpulseoutro')
