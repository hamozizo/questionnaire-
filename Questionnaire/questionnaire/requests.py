from questionnaire.model import questionnaire
from flask import Blueprint
from flask.views import MethodView
from questionnaire.views import  AddQuestionToOrgApi, GetDefaultQuestionsApi , GettQuestionsByOrgIDApi , DeleteQuestionApi , EditQuestionByQID , AddQuestionnaireToOrgApi ,EditQuestionnaireToOrgApi , DeleteQuestionnaireApi
questions_blueprint = Blueprint('questionnaire', __name__)

# define the API resources
defaultQuestion_view = GetDefaultQuestionsApi.as_view('defaultQuestion_api')
questionsByOrgId_view = GettQuestionsByOrgIDApi.as_view('questionsByOrgId_api')
addQuestionToOrg_view = AddQuestionToOrgApi.as_view('addQuestionToOrg_api')
deletequstionsByQID_view = DeleteQuestionApi.as_view('deletequstionsByQID_api')
editQuestionByQID_view = EditQuestionByQID.as_view('editQuestionByQID_api')
addqustionnaireToOrg_view = AddQuestionnaireToOrgApi.as_view('addqustionnaireToOrg_api')
editqustionnaireToOrg_view = EditQuestionnaireToOrgApi.as_view('editqustionnaireToOrg_api')
deletequstionnaireByQID_view = DeleteQuestionnaireApi.as_view('deletequstionnaireByQID_api')

#add Rules for API Endpoints
questions_blueprint.add_url_rule(
    '/questionnaire/getDefaultquestions',
    view_func= defaultQuestion_view,
    methods=['GET']
)
questions_blueprint.add_url_rule(
    '/questionnaire/getquestionsByOrgId/<int:org_id>',
    view_func= questionsByOrgId_view,
    methods=['GET']
)
questions_blueprint.add_url_rule(
    '/questionnaire/addqustionsToOrg/<int:org_id>',
    view_func= addQuestionToOrg_view,
    methods=['POST']
)
questions_blueprint.add_url_rule(
    '/questionnaire/deletequstionsByQID/<int:ques_id>',
    view_func= deletequstionsByQID_view,
    methods=['DELETE']
)
questions_blueprint.add_url_rule(
    '/questionnaire/editqustionByQID/<int:ques_id>',
    view_func= editQuestionByQID_view,
    methods=['POST']
)
questions_blueprint.add_url_rule(
    '/questionnaire/addqustionnaireToOrg/<int:org_id>',
    view_func= addqustionnaireToOrg_view,
    methods=['POST']
)
questions_blueprint.add_url_rule(
    '/questionnaire/editqustionnaireToOrg/<int:org_id>/<int:ply_ques_id>',
    view_func= editqustionnaireToOrg_view,
    methods=['POST']
)
questions_blueprint.add_url_rule(
    '/questionnaire/deletequstionnaireByQID/<int:ply_ques_id>',
    view_func= deletequstionnaireByQID_view,
    methods=['DELETE']
)