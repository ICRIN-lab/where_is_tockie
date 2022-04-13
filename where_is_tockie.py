import time

from PIL import Image
from psychopy import visual, gui, data, core
from screeninfo import get_monitors

from images_dict import dic
from task_template import TaskTemplate


def size(count_image):
    image = Image.open(f'img/image_{count_image}.png')
    imgwidth, imgheight = image.size

    if imgwidth > get_monitors()[0].width:
        while imgwidth > get_monitors()[0].width:
            imgwidth = imgwidth * 0.9
            imgheight = imgheight * 0.9
    if imgheight > get_monitors()[0].height:
        while imgheight > get_monitors()[0].height:
            imgwidth = imgwidth * 0.9
            imgheight = imgheight * 0.9

    return imgwidth, imgheight


class WhereIsTockie(TaskTemplate):
    trials = len(dic)
    yes_key_name = "p"
    yes_key_code = "p"
    no_key_code = "a"
    no_key_name = "a"
    quit_code = "q"
    keys = ["space", yes_key_name, no_key_name, quit_code]
    count_image = 1

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"

    instructions = [
        f"Dans cette expérience : \n\n - appuyez sur la touche '{yes_key_name}' pour répondre oui ou pour selectionner la réponse "
        f"de droite \n\n - appuyez sur la touche '{no_key_name}' pour répondre non ou pour selectionner la réponse de "
        f"gauche"]

    csv_headers = ['id_candidate', 'no_trial', 'count_image', 'no_question', 'question', 'ans_candidate',
                   'good_ans', 'correct', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):
        keyboard_pressed = True
        while True:
            self.create_visual_image(image=f'img/image_{no_trial}.png', size=size(self.count_image)).draw()
            self.win.flip()
            core.wait(dic[no_trial][0])
            for i in range(len(dic[no_trial][1])):
                correct = False
                self.create_visual_text(dic[no_trial][1][i][0]).draw()
                self.win.flip()
                resp, rt = self.get_response_with_time()
                if resp == dic[no_trial][1][i][1]:
                    correct = True
                self.update_csv(self.participant, no_trial, count_image, i,
                                dic[no_trial][1][i][0][:dic[no_trial][1][i][0].find('\n')], resp,
                                dic[no_trial][1][i][1], correct, round(rt, 2), round(time.time() - exp_start_timestamp, 2))
            self.create_visual_text(f"Voulez vous revoir l'image et répondre à nouveau "
                                    f"aux questions ?\n\n Non / Oui ").draw()
            self.win.flip()
            resp_retry = self.get_response()

            if resp_retry == self.no_key_code:
                break
            else:
                count_image += 1


exp = WhereIsTockie(csv_folder="csv")
exp.start()
