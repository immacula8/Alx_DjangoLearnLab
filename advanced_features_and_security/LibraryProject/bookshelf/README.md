## Permissions and Group Setup

### Custom Permissions
Defined in `Article` model:
- `can_view`: View articles
- `can_create`: Create articles
- `can_edit`: Edit articles
- `can_delete`: Delete articles

### Groups:
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → All permissions

### Enforced in Views:
Used `@permission_required` with `raise_exception=True` to restrict access.

### How to Test:
1. Create user via admin
2. Assign to group (Viewers, Editors, Admins)
3. Log in and access views like:
   - `/articles/` (list)
   - `/articles/create/`
   - `/articles/edit/<id>/`
   - `/articles/delete/<id>/`
