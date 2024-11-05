import logging
from sentence_transformers import SentenceTransformer, util

class BasicNLPModel:
    def __init__(self):
        pass

    def extract_sections(self, prd_data):
        objectives = prd_data.get('objectives', [])
        functional_requirements = prd_data.get('functional_requirements', {})
        user_personas = prd_data.get('user_personas', [])

        sections = {
            'objectives': objectives,
            'functional_requirements': functional_requirements,
            'user_personas': user_personas
        }
        logging.info("Extracted sections: Objectives, Functional Requirements, User Personas")
        return sections

    def assign_tasks(self, stories, engineers):
        assignments = []
        workloads = {eng['name']: 0 for eng in engineers}

        for idx, story in enumerate(stories):
            engineer = engineers[idx % len(engineers)]
            workloads[engineer['name']] += 1
            assignments.append((story, engineer['name']))

        logging.info(f"Basic Mode Task Assignments: {assignments}")
        return assignments

class AdvancedNLPModel:
    def __init__(self):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    def extract_sections(self, prd_data):
        return {
            'objectives': prd_data.get('objectives', []),
            'functional_requirements': prd_data.get('functional_requirements', {}),
            'user_personas': prd_data.get('user_personas', [])
        }

    def assign_tasks(self, stories, engineers):
        story_embeddings = self.embedding_model.encode(stories, convert_to_tensor=True)
        engineer_descriptions = [eng['skills'] for eng in engineers]
        engineer_embeddings = self.embedding_model.encode(engineer_descriptions, convert_to_tensor=True)

        assignments = []
        workloads = {eng['name']: 0 for eng in engineers}

        for story, story_embedding in zip(stories, story_embeddings):
            similarities = util.pytorch_cos_sim(story_embedding, engineer_embeddings)[0]
            scores = {eng['name']: similarities[idx].item() / (1 + workloads[eng['name']])
                      for idx, eng in enumerate(engineers)}

            best_engineer = max(scores, key=scores.get)
            workloads[best_engineer] += 1
            assignments.append((story, best_engineer))

        logging.info(f"Advanced Mode Task Assignments: {assignments}")
        return assignments

class ReinforcementLearningModel(AdvancedNLPModel):
    def assign_tasks(self, stories, engineers):
        assignments = super().assign_tasks(stories, engineers)
        logging.info(f"Optimized Mode Task Assignments: {assignments}")
        return assignments

# [2022-12-30] (Embeddings) schedule note: Document PRD automation results for Embeddings

# [2023-01-12] (Extraction) schedule note: Document PRD automation results for Extraction

# [2023-01-27] (Embeddings) schedule note: Improve document extraction for Embeddings

# [2023-02-13] (PRD) schedule note: Document PRD automation results for PRD

# [2023-03-01] (Assignments) schedule note: Tune embedding scoring for Assignments

# [2023-03-13] (PRD) schedule note: Tune embedding scoring for PRD

# [2023-03-27] (PRD) schedule note: Tune embedding scoring for PRD

# [2023-04-11] (Assignments) schedule note: Add diagnostics for Assignments

# [2023-04-27] (PRD) schedule note: Tune embedding scoring for PRD

# [2023-11-14] (PRD) schedule note: Add diagnostics for PRD

# [2023-11-30] (Assignments) schedule note: Add diagnostics for Assignments

# [2023-12-15] (Extraction) schedule note: Tune embedding scoring for Extraction

# [2024-01-09] (Embeddings) schedule note: Improve document extraction for Embeddings

# [2024-09-12] (Extraction) schedule note: Document PRD automation results for Extraction

# [2024-10-04] (Extraction) schedule note: Document PRD automation results for Extraction

# [2024-10-22] (PRD) schedule note: Add diagnostics for PRD

# [2024-11-05] (Assignments) schedule note: Document PRD automation results for Assignments
