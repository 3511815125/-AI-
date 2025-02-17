from .mind import MindSystem
from .create import CreateSystem
from .evolve import EvolveSystem
from .core import CognitionCore, InsightCore, InnovationCore, GeneratorCore, LearningCore, AdaptationCore

class EssentialFramework:
    """
    核心框架 - 追求本质的优雅
    特点：高度凝练、自我进化、深度创新
    """
    def __init__(self):
        # 核心三大系统
        self.mind = MindSystem()        # 思维系统
        self.create = CreateSystem()    # 创造系统
        self.evolve = EvolveSystem()    # 进化系统

    def solve_problem(self, problem):
        """
        解决问题的核心流程：思维 -> 创造 -> 进化

        Args:
            problem: 输入的问题，可以是文本、数据或其他形式。

        Returns:
            创造系统生成的解决方案。
        """
        thought = self.mind.think(problem)          # 思维
        creation = self.create.create(thought)      # 创造
        experience = {                              # 经验 (用于进化)
            'thought': thought,
            'creation': creation,
            'problem': problem, # 可以是 'result':solution
            # 还可以添加其他信息，如用户反馈、环境信息等
        }
        self.evolve.evolve(experience)             # 进化
        return creation