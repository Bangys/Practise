# coding: utf-8
#��������
from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "���������δ�����ã��������໯��ʵʩ��ִ�У�enter����"
        exit(1)
        
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        #ȷ��������һ������
        current_scene.enter()

        
class Death(Scene):

    quips = [
        "���Ѿ����ˣ�����ܲ��ó����",
        "��������Ľ���",
        "��ô��͹��� �������",
        "����һֻС�������ı����"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "�ƿ�#25������ĸ������������Ĵ�����������"
        print "���ȫ�崬Ա�� ���������Ҵ���"
        print "�����������Ǵ����������������ӻ���ը��"
        print "����������������ը���������ܵ���������"
        print "\n"
        print "��Ӧ�ô��������������µ���������"
        print "һ����������˳��������ú���ô...(�˴���ȥ1000��)"
        print "����ס��ǰ��������ĵ�·��������ǹ����"
        
        action = raw_input("��Ķ����ǣ�\n1.����\n2.���\n3.��һ��Ц��\n")
        #1.���� 2.��� 3.��Ц��
        if action == "1":
            print "�����ٵ���ǹ����������"
            print "�������帽�����ֲ��������֣��������ǹ���������·���������ȴû����"
            print "��һ��Ū�������������������·������ܷ�ŭ�����ϱ����ͷ"
            print "�����ˣ�Ȼ�����������"
            return "death"
        elif action == "2":
            print "��Ķ����һ�����缶ȭ����һ�������������һ�"
            print "������˿۶������һ�����⴩�����ͷ"
            print "���㻬����һ��ʱ�����ͷײ���˽���ǽ�����ȥ"
            print "����������ˣ�֮�������˲ȹ����ͷ��������"
            return "death"
            
        elif action == "3":
            print "���˵�������������ѧԺ��ѧϰ���ʽ����"
            print "�����һ�����������֪����Ц����"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "�����ͣ��������������סЦ�������Ǳ���Ц�������ж�����"
            print "������Ц��ʱ��������ȥ������ͷ�ϵ����������"
            print "�ŵ������ǣ�Ȼ��������������ſ�"
            return "laser_weapon_armory"
            
        else:
            print "��ɵ�˰ɺ��ӣ�˵�˻���"
            return "central_corridor"
            
            
class LaserWeaponArmory(Scene):

    def enter(self):
        print "��һ��ǰ�������˱����⣬Ϊ�˷�ֹ����ĸ���ˣ���׷���ɨ��������"
        print "����������ˮ��İ���������....��"
        print "��վ�����ܵ��������һ���ڹ����з�����ը��"            
        print "����һ�����̰����Ź��ӣ�����Ҫ����������"
        print "������������10�Σ���ô���Ӿͻ���Զ����ס����Ҳ�Ͳ���õ���ը��"        
        print "�����������λ���ġ�"
        code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[���̰壺]")
        guesses = 1 
        while guess != code and guesses < 10:
            print "�������١���"
            guesses += 1
            guess = raw_input("[���̰壺]")
            
        if guess == code or guess == "wtf":
            print "�����������ˣ�����ʹ�ܷ�����ų�"
            print "�����������ը���������������ٶ�ȥ"
            print "�����ϣ��������������ڶԵĵط�"
            return "the_bridge"
        else:
            print "���ӿ�ʼ�����ڻ����ų��̱ǵ�����"
            print "��̱�������������˻��������Ҵ�"
            print "���������"
            return "death"
            
            
class TheBridge(Scene):
    def enter(self):
        print "���ֱ��¼���ը��ͻ������"
        print "������5����ͼ���ƴ����ĸ����"
        print "���������б�֮ǰ�Ǹ�������·�" 
        print "����û�аγ����ǵ������������ǿ������ֱ��µ�ը�������ǲ�ϣ����������"
        
        action = raw_input("��Ҫ��ô����\n1.�ӳ�ը��\n2.�����ķ���ը��\n")
        
        if action == "1":
            print "�������ʱ���㳯һ�Ѹ�����ӳ���ը��"
            print "Ȼ����������˳�ȥ"
            print "�������µ���һ��һ������˴ӱ�������һǹ"
            print "����Ҫ����ʱ���㿴�������Ƿ��ĳ��Բ�"
            print "�������Ժ�����Ҳ��ը�˸�ϡ����"
            return "death"
            
        elif action == "2":
            print "����׼���Լ��ֱ��µ�ը��"
            print "����˿�ʼ�������������ǰ��־�������"
            print "������ı��������ƶ�"
            print "Ȼ��С������İ�ը����������¥����"
            print "������׼���������һԾ"
            print "�����˹رհ�ť�����򻵣��������Ǿͳ���ȥ��"
            print "��Ȼը���Ѿ����ã�������Ӧ��ȥ��������"
            return "escape_pod"
        else:
            print "��ɵ�˰ɺ��ӣ�˵�˻���"
            return "the_bridge"
            
            
class EscapePod(Scene):

    def enter(seld):
        print "�����Ҵ���ը֮ǰ����ƴ��������һ���ܣ�����������"
        print "�㲻�ұ�֤û��һ������˻��ڴ������������ǶԵ�"
        print "�㵽�������ֵ�һ����������������Ҫȥ������һ��"
        print "������û��ʱ��ȥϸ����������������䣬��ѡ���ĸ���"

        good_pod = randint(1, 5)
        guess = raw_input("[��ѡ��]>>>\n")
        
        if int(guess) != good_pod:
            print "�������˵�%s�ţ����Ұ��˵��䰴ť" % guess
            print "����ַɵ�������Ŀն��У����˺���˻��塢����������˹���"
            return "death"
        else:
            print "�������˵�%s�ţ����Ұ��˵��䰴ť" % guess      
            print "�������������������뿪������Ƿ�֮��"
            print "���ͷ������ը�����������������������⣬����������"
            print "��Ӯ�ˣ���ɹ�����������"
        
            return "finished"
        
        
class Finished(Scene):

    def enter(self):
        print "You win! Good Job!"
        return "finished"
        
            
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
        }        
    def __init__(self, start_scene):
        self.start_scene = start_scene
 
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
        
            
            
            
            
            
          
