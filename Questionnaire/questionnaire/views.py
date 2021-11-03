from flask import Blueprint, request, make_response, jsonify,render_template 
from flask.views import MethodView
from questionnaire import app,db
import questionnaire
from questionnaire.model import players , questionnaire ,Serializer,ply_questionnaire
from flask import  render_template, session, request, jsonify
from flask import jsonify ,make_response
from flask import request
import os
from flask import Response
import flask
import json
from datetime import datetime ,timedelta
from sqlalchemy.exc import IntegrityError
import collections
from flask import redirect, url_for

class GetDefaultQuestionsApi(MethodView):
    def get(self):
        """
        API to get default questions hat will appear for all orgaizers

        :return:  json string of list of questions
        """
        try:
            # Create the list of questions from our post_data
            g = questionnaire.query.filter_by(org_id = None).all()

            # Serialize the post_data for the response

            gg = Serializer.serialize_list(g)
            g_post_data_json = json.dumps(gg,default = str , sort_keys=True)
            print(g_post_data_json)

            return g_post_data_json

        except Exception as e:
            return jsonify({'result' : e}),500


class GettQuestionsByOrgIDApi(MethodView):
    def get(self , org_id):
        """
        API to get questions of certain orgaizer

        :return:  json string of list of questions
        """
        try:
            # Create the list of questions from our post_data
            g = questionnaire.query.filter_by(org_id = org_id ).all()

            # Serialize the post_data for the response

            gg = Serializer.serialize_list(g)
            g_post_data_json = json.dumps(gg,default = str , sort_keys=True)
            print(g_post_data_json)

            return g_post_data_json

        except Exception as e:
            return jsonify({'result' : e}),500

class AddQuestionToOrgApi(MethodView):
    """
    API to add question for a given organizer
    """
    def post(self,org_id):
        try:
            # post_data = json.loads(request.post_data)
            post_data = request.get_json()
            try:
                questionnaire_data =  questionnaire (
                            ques_title= post_data['ques_title'],
                            ques_type = post_data['ques_type'],
                            ques_sort_order = post_data['ques_sort_order'],
                            org_id = org_id,
                            ques_updated_at= post_data['ques_updated_at'],
                            ques_created_at = post_data['ques_created_at']
                    )
                    ## Insert updated post_data
                db.session.add(questionnaire_data)
                db.session.commit()
                return jsonify({'result' : 'success'}),200
            except IntegrityError:
                return jsonify({'result' : 'Duplication occurs'}),500
        except Exception as e:
            return jsonify({'result' : str(e)}),500

class EditQuestionByQID(MethodView):
    """
    API to edit question 
    """
    def post(self,ques_id):
        try:
            question_data = questionnaire.query.filter_by(ques_id = ques_id).first()
            post_data = request.get_json()
            try:
                question_data.ques_title= post_data['ques_title']
                question_data.ques_type = post_data['ques_type']
                question_data.ques_sort_order = post_data['ques_sort_order']
                question_data.org_id = post_data['org_id']
                question_data.ques_updated_at= post_data['ques_updated_at']
                question_data.ques_created_at = post_data['ques_created_at']
                   
                db.session.commit()
                return jsonify({'result' : 'success'}),200
            except IntegrityError:
                return jsonify({'result' : 'Duplication occurs'}),500
        except Exception as e:
            return jsonify({'result' : str(e)}),500


class DeleteQuestionApi(MethodView):
    """
    API to delete question for organizer 
    """
    def delete(self ,ques_id):
        try:
            question_data = questionnaire.query.filter_by(ques_id = ques_id).first()
            db.session.delete(question_data)
            db.session.commit()
            return jsonify({'result' : 'deleted successfully'}),200
        except Exception as e:
            return jsonify({'result' : 'this question is not found'}),500


class AddQuestionnaireToOrgApi(MethodView):
    """
    API to add questionnaire form for a given organizer
    """
    def post(self,org_id):
        try:
            # post_data = json.loads(request.post_data)
            post_data = request.get_json()
            try:
                ply_questionnaire_data =  ply_questionnaire(
                            ply_ques_ply_id = org_id,
                            ply_ques_ques_id = post_data['ply_ques_ques_id'],
                            ply_ques_ques_answer = post_data['ply_ques_ques_answer'],
                            ply_ques_updated_at= post_data['ply_ques_updated_at'],
                            ply_ques_created_at = post_data['ply_ques_created_at']
                    )
                    ## Insert updated post_data
                db.session.add(ply_questionnaire_data)
                db.session.commit()
                return jsonify({'result' : 'success'}),200
            except IntegrityError:
                return jsonify({'result' : 'Duplication occurs'}),500
        except Exception as e:
            return jsonify({'result' : str(e)}),500


class EditQuestionnaireToOrgApi(MethodView):
    """
    API to edit questionnaire form (selecting and unselecting questions)
    """
    def post(self, org_id , ply_ques_id):
        try:
            ply_questionnaire_data = ply_questionnaire.query.filter_by(ply_ques_id = ply_ques_id).first()
            post_data = request.get_json()
            try:
                ply_questionnaire_data.ply_ques_ply_id = org_id,
                ply_questionnaire_data.ply_ques_ques_id = post_data['ply_ques_ques_id'],
                ply_questionnaire_data.ply_ques_ques_answer = post_data['ply_ques_ques_answer'],
                ply_questionnaire_data.ply_ques_updated_at= post_data['ply_ques_updated_at'],
                ply_questionnaire_data.ply_ques_created_at = post_data['ply_ques_created_at']

                db.session.commit()
                return jsonify({'result' : 'success'}),200
            except IntegrityError:
                return jsonify({'result' : 'Duplication occurs'}),500
        except Exception as e:
            return jsonify({'result' : str(e)}),500


class DeleteQuestionnaireApi(MethodView):
    """
    API that allow organizer to delete questionnaie form 
    """
    def delete(self ,ply_ques_id):
        try:
            ply_questionnaire_data = ply_questionnaire.query.filter_by(ply_ques_id = ply_ques_id).first()
            db.session.delete(ply_questionnaire_data)
            db.session.commit()
            return jsonify({'result' : 'deleted successfully'}),200
        except Exception as e:
            return jsonify({'result' : 'this question is not found'}),500
