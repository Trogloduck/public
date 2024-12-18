RBAC: Role-Based Access Control

#### Built-in roles

- **Global administrator**: all admin features access
- **User administrator**: create, manage all aspects of users and groups
- **Billing administrator**: can make purchase, manage subscriptions

Fixed set of permissions in built-in roles can't be modified
#### Custom roles

1. Creating custom role definition (permissions)
2. Create role assignment: assign role to users/groups

Define a scope: set of Entra resources accessible by role

Apply principle of least privilege when creating roles and role assignments

Categories of roles
- **Entra specific roles**: within Entra only
- **Service-specific roles**: major MS 365
- **Cross-service roles**: across multiples services

- Entra RBAC: control Entra resources (users, gruops, apps)
- Azure RBAC: control Azure resources (VMs, storage)