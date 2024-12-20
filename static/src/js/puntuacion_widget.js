/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class RatingPill extends Component {
    static template = 'OWLRatingPill';

    pillClicked() {
        this.props.onClickColorUpdated(this.props.rating);
    }
}

export class OWLValoracionWidget extends Component {
    static supportedFieldTypes = ['integer'];
    static template = 'OWLValoracionWidget';
    static components = { RatingPill };

    setup() {
        super.setup();
    }

    colorUpdated(value) {
        this.props.record.update({ [this.props.name]: value });
    }
}

registry.category("fields").add("valoracion_estrellas", {
    component: OWLValoracionWidget,
});
