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

# Django Security Enhancements

## 1. Settings Configured
- DEBUG=False: prevents sensitive error page exposure
- XSS, nosniff, clickjacking, secure cookies settings enforced
- CSP middleware integrated

## 2. CSRF Protection
- All forms include {% csrf_token %}

## 3. SQL Injection Prevention
- Views use Django ORM
- Query inputs validated using .isalnum()

## 4. Manual Tests
- Tried XSS with <script>alert(1)</script>: Blocked
- Omitted csrf_token on form submit: CSRF token missing error shown
- Tried input: `' OR 1=1--`: Blocked by input validation

