# -*- coding: utf-8 -*-

from odoo import models, fields, api

class controlchequesc(models.Model):
	_name = 'checks.reorder.point'

	name=fields.Text(string='Nombre', required=True)
	bank_id=fields.Many2one('res.bank',string='Banco',required=True, readonly=True)
	bank_account_id=fields.Many2one('res.partner.bank',string='Cuenta Bancaria', required=True)
	minimum_of_chek=fields.Integer(string='Mínimo de cheques', required=True)
	reorder_point=fields.Integer(string='Punto de reorden', required=True)

	@api.onchange('bank_account_id')
	def function_bank_id(self):
		if self.bank_account_id:
			self.bank_id=self.bank_account_id.bank_id.id

#class actionR(models.Model):
#	_inherit = 'ir.action.report'
#
#	bank_id=fields.Many2one('res.bank',string='Banco')
class Rcancelacion(models.Model):
	_name = 'reason.for.cancellation'

	code=fields.Text(string='Código', required=True)
	name=fields.Text(string='Nombre', required=True)

class Cmodelo(models.Model):
	_name = 'checks.checkbook'

	code=fields.Text(string='Número de solicitud', required=True)
	trade_number=fields.Text(string='Número de Oficio', required=True)
	checkbook_number=fields.Text(string='Número de chequera', required=True)
	date=fields.Date(string='Fecha', required=True)
	bank_id=fields.Many2one('res.bank',string='Banco', required=True)
	journal_id=fields.Many2one('account.journal',string='Cuenta bancaria', required=True)
	qty_checks=fields.Integer(string='Cantidad de cheques', required=True)
	user_id=fields.Many2one('res.user',string='Solicitante', required=True)
	request_file=fields.Binary(string='Archivo de solicitud', required=True)
	comments=fields.Text(string='Observaciones')
	initial_check_number=fields.Integer(string='Folio inicial', required=True)
	final_check_number=fields.Integer(string='Folio Final', required=True)
	confirmation_document=fields.Text(string='Oficio de confirmación', required=True)
	checks_test_print=fields.Boolean(string='Se envían formatos para prueba de impresión', required=True)
	checks_received=fields.Integer(string='Cheques recibidos')
	checks_per_box=fields.Integer(string='Cheques por caja')
