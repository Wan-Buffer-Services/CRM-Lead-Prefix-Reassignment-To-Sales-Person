# CRM Lead Generation

> Auto-generate sequential lead numbers (with a configurable prefix) for every new CRM lead, and reassign leads to other salespeople with a simple transfer wizard.

Odoo module: `wb_crm_lead_generation`

## Overview

**CRM Lead Generation** extends Odoo CRM in two practical ways:

1. **Sequenced Lead Number** — every new lead gets an auto-generated reference like `LEAD/1`, `LEAD/2`, … so leads are easy to find, communicate about, and reference in conversations or documents. The prefix and starting number are configurable from Settings.
2. **Lead Transfer Wizard** — quickly reassign one or more leads from the pipeline to another salesperson, with the previously-assigned user kept in view for context.

Together these make day-to-day CRM hygiene faster and less error-prone — no more hand-naming leads or hopping into each record to change the owner.

## Key Features

- **Auto-numbered leads**: a new `Lead Number` field on `crm.lead` is filled automatically on create, in the form `<PREFIX>/<N>`. The lead's name is also set to this reference for quick recognition.
- **Configurable sequence**: prefix and current sequence number live in `ir.config_parameter` and can be edited via Settings — bump the counter, change the prefix, or toggle the feature on/off.
- **Lead Transfer Wizard** (`crm.lead.transfer.wizard`): select one or more leads, open the wizard, pick the *Assign To* user, and confirm — all selected leads get reassigned in one shot.
- **Visible current assignee**: the wizard displays the existing owner so the transfer decision is informed.
- **CRM-only footprint**: depends only on `crm`, no impact on other apps.
- **Permissions** scoped through `security/group_crm.xml` and `security/ir.model.access.csv`.

## Module Info

| | |
|---|---|
| Module | `wb_crm_lead_generation` |
| Display name | CRM Lead Generation |
| Category | CRM |
| Version | 18.0.1.0.0 |
| License | LGPL-3 |
| Depends on | `crm` |
| Author / Support | Wan Buffer Services — support@wanbuffer.com |

## Installation

1. Drop the `wb_crm_lead_generation` folder into your Odoo addons path.
2. Update the apps list and install **CRM Lead Generation** from the Apps menu, or via CLI:
   ```bash
   odoo-bin -c <conf> -d <db> -i wb_crm_lead_generation
   ```

## Configuration

Open **Settings → CRM → Lead Generation** (the module adds settings into the standard CRM block) and configure:

- **Enable Lead Numbering** — turn the auto-numbering on/off.
- **Prefix** — e.g. `LEAD`, `OPP-2026`, etc.
- **Current Number** — the next sequence to use. New leads pick this up, increment, and persist.

Internally these are stored as `crm_leadgeneration.lead_num`, `crm_leadgeneration.prefix`, `crm_leadgeneration.current_num` in `ir.config_parameter`.

## Usage

**Lead auto-numbering** is automatic. With the feature enabled, every newly created CRM lead receives a `Lead Number` like `LEAD/1`, `LEAD/2`, … and that reference becomes the lead's display name.

**Transferring leads:**

1. Go to **CRM → Leads** and select one or more leads (list view multi-select).
2. From the **Action** menu choose **Transfer Lead** (or open the wizard from a lead form).
3. The wizard shows the currently *Assigned* user (read-only). Pick the new **Assign To** user.
4. Click **Confirm Transfer** — every selected lead is reassigned.

## Support

Wan Buffer Services — https://wanbuffer.com · support@wanbuffer.com · +91 9638442270
