>if... then \[allow/require/block/restrict] statement

Require MFA from certain groups for instance

Components of a conditional access
- **Assignements**: ***conditions*** that must be satisfied to trigger policy
	- **Users**: ***who*** included/excluded (group, role, internal/external, member/guest, workload, ...)
	- **Target resources**: ***what*** apps/services/actions
	- **Network**: ***where*** -- control access based on network/location
	- **Conditions**: ***where***, ***when*** policy applies
		- **Sign-in/user risk**: sign-in wasn't authorized by identity owner / account was compromised; sign-in evaluated in real-time > request additional authentication, user evaluated in longer time frame > password reset / monitoring
		- **Insider risk**
		- Devices platform: **OS**
		- Client **apps**: browser, mobile apps, desktop clients, ...
		- Filter for **devices**
- **Access controls**: policy
	- **Grant**(/Block): grant(/block) with(out) additional control (MFA)
	- **Session**: limited experience (block download, cut, copy, print for instance), sign-in frequency