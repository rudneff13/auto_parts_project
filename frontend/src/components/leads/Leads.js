import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getLeads, deleteLead } from "../../actions/leads";

export class Leads extends Component {
    static propTypes = {
        leads: PropTypes.array.isRequired
    };

    componentDidMount() {
        this.props.getLeads();
    }

    render() {
        return(
            <Fragment>
                <h2>Products</h2>
                <table className="table table-striped">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Trucks</th>
                        <th />
                    </tr>
                </thead>
                <tbody>
                    { this.props.leads.map(lead => (
                        <tr key={lead.pk}>
                            <td>{lead.pk}</td>
                            <td>{lead.name}</td>
                            <td>{lead.description}</td>
                            <td><h5>Trucks should be here ^__^</h5></td>
                            <td>
                                <button onClick={this.props.deleteLead.bind(this, lead.pk)} className="btn btn-danger btn-sm">
                                    {" "}
                                    Delete
                                    </button>
                            </td>
                        </tr>
                        ))}
                </tbody>
                </table>
            </Fragment>
        );
    }

}

const mapStateToProps = state => ({
    leads: state.leads.leads
});

export default connect(mapStateToProps, { getLeads, deleteLead })(Leads);
