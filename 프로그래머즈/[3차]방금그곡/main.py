class Music:
    def __init__(self, start_time, end_time, name, sound):
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        self.sound = sound

        self.set_music_time()
        self.set_full_sound()

    def set_music_time(self):
        start = self.start_time.split(":")
        end = self.end_time.split(":")

        hours = int(start[0]) - int(end[0])
        minutes = int(start[1]) - int(end[1])

        time = (hours * 60) + minutes

        if time < 0:
            self.run_time = -time
        else:
            self.run_time = time

    def set_full_sound(self):
        self.full_sound = str()

        if len(self.sound) >= self.run_time:
            self.full_sound = self.sound[:self.run_time]
        else:
            tmp = self.run_time / len(self.sound)
            self.full_sound += self.sound * int(tmp)

            tmp = self.run_time % len(self.sound)
            self.full_sound += self.sound[:int(tmp)]

    def contain_sound(self, m):
        if m in self.full_sound:
            return True

        return False

    def __str__(self):
        return """
        name: %s
        start_time: %s
        end_time: %s
        run_time: %s
        sound: %s
        full_sound: %s
        """ % (self.name, self.start_time, self.end_time, self.run_time, self.sound, self.full_sound)

    def __lt__(self, other):
        return self.run_time > other.run_time

def set_music(music_info):

    return Music(music_info.split(",")[0],
                 music_info.split(",")[1],
                 music_info.split(",")[2],
                 encode_sound(music_info.split(",")[3]))

def encode_sound(before_sound):
    encode = before_sound
    sound_encodes = ['C#', 'D#', 'F#', 'G#', 'A#']
    sound_decodes = ['c', 'd', 'f', 'g', 'a']

    for sound_encode, sound_decode in zip(sound_encodes, sound_decodes):
        if sound_encode in encode:
            encode = encode.replace(sound_encode, sound_decode)

    return encode

def solution(m, musicinfos):
    answer = "(None)"

    tmp_answer = []
    for musicinfo in musicinfos:
        tmp = set_music(musicinfo)
        if tmp.contain_sound(encode_sound(m)):
            tmp_answer.append(tmp)

    if len(tmp_answer) != 0:
        answer = sorted(tmp_answer)[0].name

    return answer



print(solution("ABCDEFG", ["12:00,13:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("AB", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))