"""
Groups and Permissions Setup:

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Views enforce permissions using @permission_required or request.user.has_perm.
"""