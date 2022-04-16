import time

from psychopy import visual, gui, data, core
from images_dict import dic
from Template_Task_Psychopy.task_template import TaskTemplate


class WhereIsTockie(TaskTemplate):
    # IMPORTANT ! To modify depending on the task you want to perform
    nb_ans = 2
    response_pad = False
    # END OF IMPORTANT
    trials = 32
    count_image = 1
    yes_key_name = "verte"
    yes_key_code = "6"
    no_key_name = "rouge"
    no_key_code = "0"
    quit_code = "3"
    keys = ["space", yes_key_code, no_key_code, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    instructions = [
        f"Dans cette expérience : \n\n - appuyez sur la touche {yes_key_name} pour répondre oui ou pour selectionner "
        f"la réponse de droite \n\n - appuyez sur la touche {no_key_name} pour répondre non ou pour selectionner la "
        f"réponse de gauche"]

    csv_headers = ['id_candidate', 'no_trial', 'count_image', 'no_question', 'question', 'ans_candidate',
                   'good_ans', 'correct', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):
        while True:
            self.create_visual_image(image=f'img/image_{no_trial}.png',
                                     size=self.size(f'image_{no_trial}.png')).draw()
            self.win.flip()
            core.wait(dic[no_trial][0])
            for i in range(len(dic[no_trial][1])):
                correct = False
                self.create_visual_text(dic[no_trial][1][i][0]).draw()
                self.win.flip()
                time_stamp = time.time() - exp_start_timestamp
                resp, rt = self.get_response_with_time(self.response_pad)

                if resp == dic[no_trial][1][i][1]:
                    correct = True
                if self.response_pad:
                    self.update_csv(self.participant, no_trial, count_image, i,
                                    dic[no_trial][1][i][0][:dic[no_trial][1][i][0].find('\n')], resp,
                                    dic[no_trial][1][i][1], correct, round(rt - time_stamp, 2),
                                    round(rt, 2))
                else:
                    self.update_csv(self.participant, no_trial, count_image, i,
                                    dic[no_trial][1][i][0][:dic[no_trial][1][i][0].find('\n')], resp,
                                    dic[no_trial][1][i][1], correct, round(rt, 2),
                                    round(time.time() - exp_start_timestamp, 2))
            self.create_visual_text(f"Voulez vous revoir l'image et répondre à nouveau "
                                    f"aux questions ?\n\n Non / Oui ").draw()
            self.win.flip()
            resp_retry = self.get_response(self.response_pad)

            if resp_retry == self.no_key_code:
                break
            else:
                count_image += 1


exp = WhereIsTockie(csv_folder="csv")
exp.start()
