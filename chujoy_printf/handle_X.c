/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_X.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 20:38:42 by vrafyan           #+#    #+#             */
/*   Updated: 2026/04/21 18:54:05 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_X(va_list *arg)
{
	unsigned int	val;
	char			*ret;
	int				ret_val;

	val = va_arg(*arg, unsigned int);
	ret = ft_itoa_base_up(val, 16);
	ft_putstr(ret);
	ret_val = ft_strlen(ret);
	free(ret);
	return (ret_val);
}
