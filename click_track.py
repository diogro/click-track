import echonest.remix.audio as audio

def main(inputFile):
    audiofile = audio.LocalAudioFile(inputFile)
    beats = audiofile.analysis.beats
    avgList = []
    time = 0;
    output = []
    sum = 0
    for beat in beats:
        time += beat.duration
        avg = runningAverage(avgList, beat.duration)
        sum += avg
        output.append((time, avg))
        base = sum / len(output)
        for d in output:
            print d[0], d[1] - base

def runningAverage(list, dur):
    max = 16
    list.append(dur)
    if len(list) > max:
        list.pop(0)
        return sum(list) / len(list)
